# role-skill-generator

一个给当前仓库配套的子项目：把“open-source deep research”的常见工作流改写成“人物经典语录 + 性格资料 + 决策风格”的结构化蒸馏流水线，并把结果直接渲染成仓库现有 persona 目录格式。

## 这个子项目解决什么

它不是再做一份通用长报告，而是把人物研究压成仓库真正需要的三层产物：

1. 检索计划：围绕语录、第一手表达、性格外评、决策方式、时间线生成 query pack。
2. 结构化 bundle：把抓回来的资料合成为 `persona bundle JSON`。
3. 仓库材料：输出 `SKILL.md`、`README.md`、`references/research/*.md`，目录格式和当前仓库一致。

## 方法文档

* [open-source-deep-research-survey.md](./docs/open-source-deep-research-survey.md)
* [persona-deep-research-method.md](./docs/persona-deep-research-method.md)

## 安装

子项目零三方依赖，直接用 Python 标准库即可：

```bash
cd role-skill-generator
python3 -m compileall src
```

## 测试

当前子项目按“可离线、可重复、先锁行为再扩功能”的思路组织测试：

* 单元测试锁 `target profile` 默认值、query pack 覆盖面、bundle 校验。
* golden fixture 锁完整渲染输出，防止 markdown 结构悄悄漂移。
* 测试不依赖网络，也不调用真实模型。

运行：

```bash
cd role-skill-generator
python3 -m unittest discover -s tests
```

如果你要跑 `synthesize` / `generate`，还需要一个 OpenAI-compatible API：

```bash
export ROLE_SKILL_OPENAI_API_KEY=...
# 可选
export ROLE_SKILL_OPENAI_BASE_URL=https://api.openai.com/v1
export ROLE_SKILL_OPENAI_MODEL=gpt-4.1-mini
```

如果你要跑联网检索，也可以选不同搜索 provider：

```bash
# 默认 duckduckgo-html，不需要 key，但稳定性一般
export TAVILY_API_KEY=...
export SERPER_API_KEY=...
```

## 命令

### 1. 生成 query pack

```bash
cd /Volumes/T7/Ten\ thousand\ soul\ banners/role-skill-generator
PYTHONPATH=src python3 -m role_skill_generator plan-queries \
  examples/ada-lovelace.target.json \
  --output examples/ada-lovelace.query-pack.md
```

### 2. 只做格式渲染

```bash
cd /Volumes/T7/Ten\ thousand\ soul\ banners/role-skill-generator
PYTHONPATH=src python3 -m role_skill_generator render \
  examples/ada-lovelace.bundle.json \
  examples/rendered
```

### 3. 跑检索抓取

```bash
cd /Volumes/T7/Ten\ thousand\ soul\ banners/role-skill-generator
PYTHONPATH=src python3 -m role_skill_generator collect \
  examples/ada-lovelace.target.json \
  runs/ada-lovelace \
  --provider duckduckgo-html \
  --max-results 4 \
  --max-documents 8
```

### 4. 合成 bundle

```bash
cd /Volumes/T7/Ten\ thousand\ soul\ banners/role-skill-generator
PYTHONPATH=src python3 -m role_skill_generator synthesize \
  examples/ada-lovelace.target.json \
  runs/ada-lovelace/documents.jsonl \
  runs/ada-lovelace/persona.bundle.json
```

### 5. 端到端生成

输出到仓库真实 persona 根目录时，把 `output_root` 指向 `soulbanner_skills/` 或 `sovereign_skills/`：

```bash
cd /Volumes/T7/Ten\ thousand\ soul\ banners/role-skill-generator
PYTHONPATH=src python3 -m role_skill_generator generate \
  examples/ada-lovelace.target.json \
  runs/ada-lovelace \
  /Volumes/T7/Ten\ thousand\ soul\ banners/soulbanner_skills \
  --provider tavily
```

## 输入约定

### `target profile JSON`

最少要有：

* `display_name`
* `classification`
* `category_tags`

其余如 `slug`、`triggers`、`source_scope`、`known_aliases`、`research_focus` 都可以显式给，也可以让工具补默认值。见：

* [ada-lovelace.target.json](./examples/ada-lovelace.target.json)

### `persona bundle JSON`

这是渲染器的直接输入，也是 `synthesize` 的输出目标。见：

* [ada-lovelace.bundle.json](./examples/ada-lovelace.bundle.json)

## 输出格式

渲染结果固定是：

```text
<slug>/
├── SKILL.md
├── README.md
└── references/
    └── research/
        ├── 01-writings.md
        ├── 02-conversations.md
        ├── 03-expression-dna.md
        ├── 04-external-views.md
        ├── 05-decisions.md
        └── 06-timeline.md
```

这和仓库根目录现有角色目录保持一致；不会额外塞进非模板要求文件。

## 设计取舍

* 检索阶段优先“证据表”而不是“漂亮长文”，因为本仓库真正消费的是 persona 结构，不是研究报告本身。
* 语录检索单独做 provenance 管控，避免假名言直接进 `SKILL.md`。
* bundle 是中间层，目的是把联网抓取和 markdown 渲染解耦，便于人工复核。
