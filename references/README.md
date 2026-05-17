# References

本目录保存与“论文配图能力”直接相关的外部参考材料。原则是只放可迁移的规范、prompt、样例和少量代表文件，不把完整工程依赖搬进来。

## paperbanana

来源：`llmsresearch/paperbanana`

用途：学习论文方法图的生成流程、评价标准、参考图检索和视觉规范。

优先阅读：

- `README.md`：整体流程，包含 Optimizer / Retriever / Planner / Stylist / Visualizer / Critic 管线。
- `guidelines/methodology_style_guide.md`：方法图视觉规范，适合转化为本项目的设计规则。
- `guidelines/plot_style_guide.md`：统计图视觉规范。
- `prompts/diagram/planner.txt`：如何把论文方法段转成详细图像描述。
- `prompts/diagram/stylist.txt`：如何把结构描述转成出版级视觉规格。
- `prompts/diagram/critic.txt`：如何做图像内容与呈现审查。
- `prompts/evaluation/faithfulness.txt`：检查图是否忠实于论文内容。
- `prompts/evaluation/conciseness.txt`：检查图是否只是“正文装盒子”。
- `prompts/evaluation/readability.txt`：检查图是否适合论文版面。
- `reference_sets/index.json` 与 `reference_sets/images/`：高质量论文图参考集。
- `examples/*.yaml`：批量生成和多子图组合的 manifest 结构。

## paper-card

来源：`~/Desktop/文稿处理/paper-card`

用途：学习学术内容视觉化、中文排版、长图信息层级和内容转译方式。它不完全是 SCI 论文配图项目，但对“复杂学术内容如何压缩为视觉结构”有参考价值。

优先阅读：

- `README.md`：项目定位。
- `CLAUDE.md`：项目内协作和实现约束。
- `docs/project-overview.md`：信息架构和产品思路。
- `case-study.html` / `index.html`：视觉化成品参考。
- `specs/001-paper-index/`：需求、计划、任务拆解方式。

## diagramming-skill

来源：`~/.hermes/skills/diagramming`

用途：补充通用图示思维和技能说明。当前只保留 `DESCRIPTION.md`，作为轻量参考。

## local examples

当前项目自己的 SCI 图例放在：

```text
../examples/education_ai_sci/
```

这些文件是当前“教育 AI SCI 论文”四张图的已导出 HTML + PNG，可作为最贴近本项目目标的本地范例。

