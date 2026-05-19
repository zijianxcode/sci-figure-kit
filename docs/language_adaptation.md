# 中英文论文图适配规则

论文图的英文版不能只做逐字翻译。英文标签通常更长，词间空格更多，缩写更多，对齐和换行方式也不同。这个项目把语言适配当作出图流程的一部分。

## 输出要求

每张正式图至少保留三种格式：

- `.html`：浏览器预览和调试
- `.svg`：矢量源文件，可拖入 Figma 继续手动编辑
- `.png`：论文、Word、PDF、PPT 中的稳定嵌入版本

英文版和中文版应当分别保留 SVG，不要只保存最终 PNG。

## 中文版规则

- 优先使用短中文概念词，不把完整句子放进图里。
- 中文标签可以更紧凑，但仍要避免一格塞两层解释。
- 推荐字体：`PingFang SC`、`Heiti SC`、`Noto Sans CJK SC`。
- 中文图适合用 18-24px 的主体字号，A4 宽度下仍应可读。

## 英文版规则

- 英文标签优先使用名词短语，例如 `Type Effects`、`Theory Gap`、`Control Rights`。
- 避免把中文长句直译成完整英文句子。先压缩为 claim，再放进图。
- 重要概念可以保留缩写：`H`、`A`、`J`、`T`、`RQ`、`SRL`。
- 英文版通常需要更小字号、更宽盒子、更明确换行。
- 推荐字体：`Source Sans 3`、`Inter`、`Helvetica Neue`、`Arial`。

## 英文换行策略

英文换行优先按语义切分：

```text
Cognitive Control Rights Distribution
Coding Scheme
```

不要机械按字数截断。短语应尽量保持完整，例如：

```text
Design-cognition decision node
Human-AI design collaboration
Operational link
```

## 色彩和语义一致性

中英文版必须共享同一套颜色语义：

- 蓝色：人类主导、研究框架、基础路径
- 金色：效果差异、权衡、比较
- 绿色：系统视角、适配、汇聚
- 紫色：共同协商、理论透镜、扩展
- 玫瑰色：缺口、动态切换、需补充部分

不要因为换语言而改变颜色含义。

## Figma 编辑规则

- `figma_editable/` 保存中文 SVG。
- `figma_editable/en/` 保存英文 SVG。
- 生成后将 SVG 拖入 Figma，右键 Ungroup，即可编辑文字、色块、箭头和线条。
- 最终论文或报告仍建议嵌入 PNG，避免不同软件对 SVG 字体渲染不一致。

## 生成命令

默认生成中文版：

```bash
python3 build_figures.py
```

只生成英文版：

```bash
python3 build_figures.py --language en --output-dir outputs/en
```

同时生成中英文版：

```bash
python3 build_figures.py --language both --output-dir outputs/bilingual
```

生成 SVG 但不同步到 `figma_editable/`：

```bash
python3 build_figures.py --language en --no-figma-sync
```
