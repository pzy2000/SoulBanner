from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from role_skill_generator.models import (
    ValidationError,
    load_json,
    normalize_persona_bundle,
    normalize_target_profile,
)
from role_skill_generator.query_pack import build_query_pack
from role_skill_generator.render import render_bundle_to_directory


class GeneratorTests(unittest.TestCase):
    def test_target_profile_applies_defaults(self) -> None:
        target = normalize_target_profile(
            {
                "display_name": "Ada Lovelace",
                "classification": "公众人物 / 数学家 / 计算先驱",
                "category_tags": ["research-flag"],
            }
        )
        self.assertEqual(target["slug"], "ada-lovelace")
        self.assertEqual(target["target_root"], "soulbanner_skills")
        self.assertRegex(target["updated_at"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertIn("Ada Lovelace", target["known_aliases"])
        self.assertEqual(len(target["triggers"]), 2)

    def test_query_pack_covers_quote_and_personality_tracks(self) -> None:
        target = normalize_target_profile(load_json(ROOT / "examples" / "ada-lovelace.target.json"))
        query_pack = build_query_pack(target)
        names = {item["name"] for item in query_pack}
        self.assertEqual(len(query_pack), 6)
        self.assertIn("quote-bank-primary", names)
        self.assertIn("personality-and-external-views", names)
        self.assertTrue(any("名言" in query for group in query_pack for query in group["queries"]))
        self.assertTrue(any("personality" in query for group in query_pack for query in group["queries"]))

    def test_render_outputs_repo_shape(self) -> None:
        bundle = normalize_persona_bundle(load_json(ROOT / "examples" / "ada-lovelace.bundle.json"))
        with tempfile.TemporaryDirectory() as tmp_dir:
            persona_dir = render_bundle_to_directory(bundle, tmp_dir)
            self.assertTrue((persona_dir / "SKILL.md").exists())
            self.assertTrue((persona_dir / "README.md").exists())
            self.assertTrue((persona_dir / "references" / "research" / "01-writings.md").exists())
            self.assertTrue((persona_dir / "references" / "research" / "06-timeline.md").exists())
            skill_text = (persona_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn('name: "ada-lovelace"', skill_text)
            self.assertIn('# 角色定位', skill_text)
            self.assertNotIn("sources.md", "\n".join(path.name for path in persona_dir.iterdir()))

    def test_render_matches_golden_fixture(self) -> None:
        bundle = normalize_persona_bundle(load_json(ROOT / "examples" / "ada-lovelace.bundle.json"))
        expected_root = ROOT / "examples" / "rendered" / "ada-lovelace"
        with tempfile.TemporaryDirectory() as tmp_dir:
            actual_root = render_bundle_to_directory(bundle, tmp_dir)
            expected_files = self._relative_file_map(expected_root)
            actual_files = self._relative_file_map(actual_root)
            self.assertEqual(actual_files, expected_files)

    def test_bundle_validation_rejects_incomplete_payload(self) -> None:
        with self.assertRaises(ValidationError):
            normalize_persona_bundle(
                {
                    "display_name": "Ada Lovelace",
                    "classification": "公众人物 / 数学家 / 计算先驱",
                    "category_tags": ["research-flag"],
                }
            )

    def _relative_file_map(self, root: Path) -> dict[str, str]:
        return {
            path.relative_to(root).as_posix(): path.read_text(encoding="utf-8")
            for path in sorted(root.rglob("*"))
            if path.is_file()
        }


if __name__ == "__main__":
    unittest.main()
