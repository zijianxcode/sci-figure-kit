# SCI Figure Kit

面向论文正文与学术报告的长期复用配图项目。当前版本从“教育 AI SCI 论文”四张图中抽离出来，目标是把学术图从“正文搬运”改成“结构提纯”。

## 项目结构

```text
sci-figure-kit/
├── build_figures.py                 # 生成 HTML + PNG 的主脚本
├── docs/
│   ├── figure_design_guide.md        # 论文图设计原则
│   ├── project_scope.md              # 项目边界和长期维护原则
│   ├── review_checklist.md           # 出图前检查清单
│   └── workflows.md                  # 论文图 / 报告图复用流程
├── examples/
│   └── education_ai_sci/             # 当前论文四张图的已导出示例
├── references/                       # 外部参考项目的重要文件
│   ├── paperbanana/                  # 论文方法图生成流程、prompt、参考图
│   ├── paper-card/                   # 学术内容视觉化和中文排版参考
│   └── diagramming-skill/            # 通用图示技能说明
├── templates/                        # 新图 brief、spec、review prompt
└── outputs/
    └── current/                      # 默认生成目录
```

## 使用

```bash
python3 build_figures.py
```

默认输出到：

```text
outputs/current/
```

指定输出目录：

```bash
python3 build_figures.py --output-dir outputs/test
```

脚本会同时生成三种文件：

- `.html`：浏览器预览和排版调试
- `.svg`：Figma 可编辑格式，优先用于继续设计
- `.png`：论文 / Word / PDF 插图使用

脚本会生成四类图：

- `fig_research_framework`：研究问题与假设关系
- `fig_literature_funnel`：文献线索汇聚与研究定位
- `fig_theory_radar`：理论适配矩阵
- `fig_framework_matrix`：四节点 × 三状态 + T 动态切换编码框架

## 当前设计原则

- 图只承担一个任务，不把章节大纲整张搬进去。
- 图内保留关键词，解释放正文或图注。
- H/A/J 是同一层级的控制权状态，T 是动态切换指标，不与 H/A/J 并列。
- 理论比较优先用定性矩阵，避免无方法支撑的主观雷达评分。
- 输出采用 16:9 矩形，减少论文排版中的竖向浪费。

## 长期复用入口

新论文或新报告开始前，先复制：

- [templates/figure_brief.md](templates/figure_brief.md)
- [templates/figure_spec.yaml](templates/figure_spec.yaml)

然后按 [docs/workflows.md](docs/workflows.md) 走一遍。

如果是从论文图改报告图，优先看 `docs/workflows.md` 里的“从论文图转报告图”。

## Figma 编辑

Figma 可编辑文件集中放在：

```text
figma_editable/
```

使用方式：

1. 打开 Figma。
2. 将 `.svg` 文件拖入画布。
3. 右键 Ungroup，按需拆解。
4. 文字、色块、线条、箭头都可以继续编辑。

注意：

- 论文或报告里最终嵌入仍建议用 PNG，避免不同软件对 SVG 字体渲染不一致。
- Figma 内若字体替换，优先使用 PingFang SC / Noto Sans CJK SC / Arial。
- 不要把 PNG 拖进 Figma 当作可编辑源文件，PNG 只能作为预览图。

## 参考材料

外部项目的关键参考文件已整理到：

[references/README.md](references/README.md)

## 依赖

- Python 3
- Google Chrome，用于 headless 截图导出 PNG
