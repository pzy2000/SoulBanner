# 万魂幡.Skill

万魂幡.Skill 是一个把公开素材中的稳定表达风格、判断习惯、叙事张力与人设特征蒸馏成 `.skill` 的多人仓库。它是一个“赛博人格样板房 / 二创 skill monorepo”，不是“数字永生工程”，更不是对真人或角色的真实性替身复制。

## 仓库定位

这个仓库面向三类对象：

* 公众人物
* 网络人物
* 虚构角色

我们的目标是把人物的稳定风格整理为：

* 可安装
* 可触发
* 可分类浏览
* 可扩展提 PR
* 可做二创整活
* 但边界明确

## 命名解释

### 为什么叫“万魂幡”

“万魂幡”是本仓库的世界观包装名，用来指代一个多人 `.skill` 集合仓库。这里的“魂”是对“人格样式 / 表达模板 / 叙事外壳”的戏谑说法，不代表真实“招魂”、真实“永生”或任何超自然能力。

### 为什么有“人皇旗（Power Figures）”

“人皇旗（Power Figures）”是仓库内部的戏谑分类标签，用于归纳那些在公共叙事中呈现出强意志、强输出、强个人品牌、强支配感的角色。该命名不代表现实能力评级、道德判断、基因优劣或政治立场背书。

### 分类不是现实评价体系

无论是“万魂幡”还是“人皇旗”，都只是二创命名：

* 不代表真实性能排序
* 不代表基因优劣
* 不代表现实价值判断
* 不构成现实背书

## 风险与边界

所有角色回答都只代表基于公开素材蒸馏出的二创视角，不替代真人，不保证时效事实正确，也不应用于冒充、诈骗、误导、政治欺诈或其他欺骗性场景。

本仓库明确反对以下表述：

* “已经实现数字永生”
* “完全复活本人”
* “百分百等于真人”

推荐理解方式：

* 以 skill 的形式复刻公开人格特征
* 把人物风格蒸馏成可调用模块
* 赛博人格样板房

## 当前角色

### 万魂幡总入口

* `all-personas`：总 skill，用于列人、按分类浏览、路由切换与多角色对比入口

### 首批人物

* `changshu-arno`：常熟阿诺，抽象梗感与“诺言诺语”风格样板
* `liangzi`：良子（李占良），草根吃播与强体感表达样板
* `tong-jincheng`：童锦程，江湖情感军师视角样板
* `trump`：特朗普，人皇旗成员，夸张对抗型叙事
* `musk`：马斯克，人皇旗成员，第一性原理与工程愿景型叙事
* `yu-dazui`：余大嘴，发布会 / 商战 / 技术话术型输出
* `hanli`：韩立，虚构角色，《凡人修仙传》中的谨慎生存流样板

更多信息见 [PEOPLE.md](PEOPLE.md) 与 `categories/`。

## 仓库结构

```text
.
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── PEOPLE.md
├── categories/
├── skills/
│   ├── all-personas/
│   ├── changshu-arno/
│   ├── liangzi/
│   ├── tong-jincheng/
│   ├── trump/
│   ├── musk/
│   ├── yu-dazui/
│   └── hanli/
├── templates/
│   └── research/
└── .github/
```

## 安装与使用

### 安装整个仓库

```bash
git clone <your-fork-or-this-repo-url> wanhunfan-skill
cd wanhunfan-skill
```

### 安装单人物 skill

以 Codex 本地技能目录为例：

```bash
cp -R skills/tong-jincheng ~/.codex/skills/tong-jincheng
```

如果你使用的是其他支持 `SKILL.md` 的客户端，也可以直接导入对应人物目录。

### 激活总 skill

将 `skills/all-personas/` 安装到你的 skill 目录后，可通过以下方式触发：

* `列出万魂幡里所有角色`
* `谁适合分析这个问题`
* `切到常熟阿诺模式`
* `用人皇旗的视角看这件事`

### 分类浏览入口

* [categories/renhuang-flag.md](categories/renhuang-flag.md)
* [categories/abstract-flag.md](categories/abstract-flag.md)
* [categories/jianghu-flag.md](categories/jianghu-flag.md)
* [categories/business-flag.md](categories/business-flag.md)
* [categories/fiction-flag.md](categories/fiction-flag.md)

## 社区扩展

欢迎继续往“万魂幡”里加人，但新增人物必须满足以下要求：

* 遵循统一模板
* 补齐 research 六件套
* 写清楚诚实边界
* 声明分类归属
* 不得把二创人格写成“真实复活”

具体规范见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

默认使用 [MIT License](LICENSE)。
