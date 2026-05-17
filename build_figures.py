#!/usr/bin/env python3
"""Build compact paper figures from SVG sources and export PNGs."""

from __future__ import annotations

import argparse
import html
import shutil
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "outputs" / "current"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")

FONT = '"PingFang SC", "Heiti SC", "Noto Sans CJK SC", Arial, sans-serif'
TEXT = "#1f2933"
MUTED = "#6b7280"
LIGHT = "#f8fafc"
LINE = "#cbd5e1"
BLUE = "#3b6f9f"
BLUE_BG = "#eaf3fb"
GREEN = "#3c7a58"
GREEN_BG = "#edf7f0"
PEACH = "#b66a45"
PEACH_BG = "#fff1e8"
PURPLE = "#6f5aa8"
PURPLE_BG = "#f2eefb"
ROSE = "#b85c6a"
ROSE_BG = "#fff0f2"
GOLD = "#9a7330"
GOLD_BG = "#fbf4df"
GRAY_BG = "#f4f6f8"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def svg_doc(width: int, height: int, body: str) -> str:
    return f"""<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="#52616f"/>
    </marker>
    <marker id="arrow-green" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">
      <path d="M0,0 L10,4 L0,8 Z" fill="{GREEN}"/>
    </marker>
    <style>
      text {{ font-family: {FONT}; }}
      .small {{ fill: {MUTED}; font-size: 18px; }}
      .label {{ fill: {TEXT}; font-size: 23px; font-weight: 650; }}
      .micro {{ fill: {MUTED}; font-size: 16px; }}
    </style>
  </defs>
  <rect width="100%" height="100%" fill="white"/>
{body}
</svg>"""


def html_doc(title: str, svg: str, width: int, height: int) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>{esc(title)}</title>
<style>
  html, body {{
    margin: 0;
    width: {width}px;
    height: {height}px;
    overflow: hidden;
    background: white;
  }}
  svg {{
    display: block;
    width: {width}px;
    height: {height}px;
  }}
</style>
</head>
<body>
{svg}
</body>
</html>
"""


def extract_svg(html_text: str) -> str:
    start = html_text.index("<svg")
    end = html_text.index("</svg>") + len("</svg>")
    return html_text[start:end] + "\n"


def rect(x: int, y: int, w: int, h: int, fill: str, stroke: str = LINE, r: int = 18,
         sw: float = 2, dash: str | None = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash_attr}/>'
    )


def line(x1: int, y1: int, x2: int, y2: int, color: str = "#52616f",
         sw: float = 2, marker: str = "arrow", dash: str | None = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker_attr = f' marker-end="url(#{marker})"' if marker else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{color}" stroke-width="{sw}" fill="none"{dash_attr}{marker_attr}/>'
    )


def path(d: str, color: str = "#52616f", sw: float = 2, marker: str = "arrow",
         dash: str | None = None) -> str:
    dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
    marker_attr = f' marker-end="url(#{marker})"' if marker else ""
    return f'<path d="{d}" stroke="{color}" stroke-width="{sw}" fill="none"{dash_attr}{marker_attr}/>'


def text(x: int, y: int, content: str, size: int = 22, color: str = TEXT,
         weight: int | str = 400, anchor: str = "middle") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}">{esc(content)}</text>'
    )


def multiline(x: int, y: int, lines: list[str], size: int = 18, color: str = MUTED,
              weight: int | str = 400, anchor: str = "middle", leading: int | None = None) -> str:
    leading = leading or int(size * 1.35)
    out = [
        f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}">'
    ]
    for i, part in enumerate(lines):
        dy = 0 if i == 0 else leading
        out.append(f'<tspan x="{x}" dy="{dy}">{esc(part)}</tspan>')
    out.append("</text>")
    return "".join(out)


def pill(x: int, y: int, w: int, h: int, label: str, fill: str, stroke: str,
         sub: str | None = None) -> str:
    cy = y + h // 2
    if sub:
        return "\n".join([
            rect(x, y, w, h, fill, stroke, 16, 2),
            text(x + w // 2, cy - 8, label, 22, TEXT, 700),
            text(x + w // 2, cy + 24, sub, 16, MUTED, 400),
        ])
    return "\n".join([
        rect(x, y, w, h, fill, stroke, 16, 2),
        text(x + w // 2, cy + 8, label, 22, TEXT, 700),
    ])


def build_research_framework() -> tuple[str, int, int]:
    w, h = 1600, 900
    body: list[str] = []
    body.append(rect(70, 52, 1460, 100, BLUE_BG, "#9bbbd5", 22))
    body.append(text(800, 88, "认知控制权分布编码方案", 26, BLUE, 750))
    body.append(text(800, 122, "四个决策节点 × H/A/J 状态，T 作为动态切换指标", 19, MUTED))
    body.append(line(800, 152, 800, 198, GREEN, 3, "arrow-green"))

    rq_boxes = [
        (120, 215, "RQ1 模式识别", ["认知控制权在四节点上的分布", "呈现哪些典型类型？"], BLUE_BG, BLUE),
        (605, 215, "RQ2 效果差异", ["不同协作类型在设计产出质量", "和设计思维提升上是否不同？"], GOLD_BG, GOLD),
        (1090, 215, "RQ3 个体关联", ["哪些个体特征与协作类型", "存在系统性关联？"], GREEN_BG, GREEN),
    ]
    for x, y, title, lines_, fill, stroke in rq_boxes:
        body.append(rect(x, y, 390, 118, fill, stroke, 18, 2.3))
        body.append(text(x + 195, y + 43, title, 25, stroke, 750))
        body.append(multiline(x + 195, y + 75, lines_, 17, TEXT))
    body.append(line(510, 274, 590, 274, GREEN, 3, "arrow-green"))
    body.append(line(995, 274, 1075, 274, GREEN, 3, "arrow-green"))
    body.append(text(800, 370, "H1 是类型学前提，H2-H6 依赖 RQ1 的分类结果", 20, ROSE, 650))
    body.append(path("M315 333 C315 390 800 390 800 430", ROSE, 2.5, "arrow", "8 7"))
    body.append(path("M800 333 C800 390 800 390 800 430", ROSE, 2.5, "arrow", "8 7"))
    body.append(path("M1285 333 C1285 390 800 390 800 430", ROSE, 2.5, "arrow", "8 7"))

    groups = [
        (120, 450, 390, 220, "H1", "类型存在性", ["至少存在三种可区分类型", "H-dominant / A-dominant / J-dominant"], BLUE_BG, BLUE),
        (565, 450, 470, 220, "H2-H4", "类型效果差异", ["H2 发散阶段：J > A，新颖性", "H3 收敛阶段：H > A，可行性与完整性", "H4 A 型速度更快，但后测较低"], GOLD_BG, GOLD),
        (1090, 450, 390, 220, "H5-H6", "个体因素与动态切换", ["H5 自我效能 / AI经验 / SRL", "H6 探索型认知风格对应更高 T 频率"], GREEN_BG, GREEN),
    ]
    for x, y, width, height, code, title_, lines_, fill, stroke in groups:
        body.append(rect(x, y, width, height, fill, stroke, 18, 2))
        body.append(text(x + 30, y + 42, code, 23, stroke, 800, "start"))
        body.append(text(x + width // 2, y + 74, title_, 23, TEXT, 750))
        body.append(multiline(x + width // 2, y + 123, lines_, 18, TEXT))

    body.append(rect(250, 730, 1100, 86, GRAY_BG, "#d7dde5", 18))
    body.append(text(800, 763, "实证链条", 22, MUTED, 700))
    body.append(text(800, 797, "识别类型 → 比较后果 → 解释个体条件", 24, TEXT, 700))
    return html_doc("fig_research_framework", svg_doc(w, h, "\n".join(body)), w, h), w, h


def build_literature_funnel() -> tuple[str, int, int]:
    w, h = 1600, 900
    body: list[str] = []
    streams = [
        (95, 90, "线索一", "概念设计认知", ["协议分析", "认知过程分类", "认知风格"], BLUE_BG, BLUE),
        (605, 90, "线索二", "人-AI 协作设计", ["非线性协作", "控制权与代理权", "协作类型学"], GOLD_BG, GOLD),
        (1115, 90, "线索三", "AI 对设计教育的影响", ["增强与侵蚀", "角色转变", "个体差异"], GREEN_BG, GREEN),
    ]
    for x, y, tag, title_, items, fill, stroke in streams:
        body.append(rect(x, y, 390, 235, fill, stroke, 20, 2.2))
        body.append(text(x + 28, y + 42, tag, 18, stroke, 700, "start"))
        body.append(text(x + 195, y + 82, title_, 27, TEXT, 760))
        for i, item in enumerate(items):
            body.append(pill(x + 45, y + 115 + i * 36, 300, 28, item, "white", "#d2dbe5"))

    for sx in [290, 800, 1310]:
        body.append(path(f"M{sx} 325 C{sx} 405 800 410 800 470", "#52616f", 2.5, "arrow"))

    body.append(rect(300, 455, 1000, 135, PURPLE_BG, PURPLE, 22, 2.5))
    body.append(text(800, 502, "分布式认知视角", 30, PURPLE, 780))
    body.append(text(800, 540, "将个体中心解释转为认知系统层面的过程分析", 21, TEXT, 500))
    body.append(line(800, 590, 800, 642, GREEN, 3, "arrow-green"))

    body.append(rect(115, 660, 1370, 155, ROSE_BG, ROSE, 22, 2.4, "12 8"))
    body.append(text(800, 700, "研究缺口与本研究定位", 26, ROSE, 760))
    gaps = [
        (175, "理论缺口", "异质人-AI系统缺少可操作概念"),
        (610, "实证缺口", "类型学尚未进入设计教育场景"),
        (1045, "教育缺口", "双面效应缺少过程-效果关联"),
    ]
    for x, title_, sub in gaps:
        body.append(rect(x, 728, 335, 58, "white", "#e5b4bb", 14, 1.8))
        body.append(text(x + 168, 750, title_, 20, TEXT, 720))
        body.append(text(x + 168, 776, sub, 15, MUTED))
    return html_doc("fig_literature_funnel", svg_doc(w, h, "\n".join(body)), w, h), w, h


def build_theory_matrix() -> tuple[str, int, int]:
    w, h = 1600, 900
    body: list[str] = []
    cols = [
        ("分析单元", "个体 → 系统"),
        ("AI交互解释", "输出如何进入决策"),
        ("控制权描述", "谁主导关键节点"),
        ("动态过程", "是否捕捉切换"),
        ("操作化接口", "可编码 / 可测量"),
    ]
    rows = [
        ("SRL", "自我调节学习", ["个体", "弱", "弱", "中", "中"], GRAY_BG, "#a8b1bd"),
        ("TAM / UTAUT", "技术接受模型", ["个体", "弱", "弱", "弱", "强"], GRAY_BG, "#a8b1bd"),
        ("Self-efficacy", "自我效能理论", ["个体", "弱", "弱", "弱", "中"], GRAY_BG, "#a8b1bd"),
        ("Distributed cognition", "分布式认知", ["系统", "强", "可扩展", "强", "需补充"], GREEN_BG, GREEN),
    ]

    x0, y0 = 150, 88
    left_w, col_w, row_h = 280, 220, 115
    body.append(rect(x0, y0, left_w + col_w * 5, 74, "#f5f7fa", "#d6dee8", 16, 2))
    for i, (title_, sub) in enumerate(cols):
        x = x0 + left_w + i * col_w
        body.append(text(x + col_w // 2, y0 + 32, title_, 20, TEXT, 750))
        body.append(text(x + col_w // 2, y0 + 58, sub, 15, MUTED))
        body.append(line(x, y0, x, y0 + 74 + row_h * 4, "#d6dee8", 1.3, marker=""))

    def score_mark(value: str, cx: int, cy: int, highlight: bool) -> str:
        colors = {
            "强": (GREEN, GREEN_BG),
            "中": (GOLD, GOLD_BG),
            "弱": ("#9aa4af", "#eef1f4"),
            "系统": (GREEN, GREEN_BG),
            "个体": ("#8b95a1", "#eef1f4"),
            "可扩展": (PURPLE, PURPLE_BG),
            "需补充": (ROSE, ROSE_BG),
        }
        stroke, fill = colors[value]
        radius = 24 if len(value) <= 2 else 38
        return "\n".join([
            f'<ellipse cx="{cx}" cy="{cy}" rx="{radius}" ry="24" fill="{fill}" stroke="{stroke}" stroke-width="{2.4 if highlight else 1.8}"/>',
            text(cx, cy + 7, value, 18, stroke, 750),
        ])

    for r, (name, sub, values, fill, stroke) in enumerate(rows):
        y = y0 + 74 + r * row_h
        body.append(rect(x0, y, left_w + col_w * 5, row_h, fill, stroke, 0, 1.5))
        body.append(text(x0 + 24, y + 45, name, 21, TEXT, 760, "start"))
        body.append(text(x0 + 24, y + 75, sub, 16, MUTED, 400, "start"))
        for i, val in enumerate(values):
            cx = x0 + left_w + i * col_w + col_w // 2
            body.append(score_mark(val, cx, y + row_h // 2, stroke == GREEN))

    body.append(rect(260, 728, 1080, 82, BLUE_BG, BLUE, 18, 2))
    body.append(text(800, 761, "关键判断", 21, BLUE, 760))
    body.append(text(800, 792, "分布式认知最适合作为分析单元，但仍需“认知控制权分布”完成操作化", 22, TEXT, 700))
    return html_doc("fig_theory_radar", svg_doc(w, h, "\n".join(body)), w, h), w, h


def build_framework_matrix() -> tuple[str, int, int]:
    w, h = 1600, 900
    body: list[str] = []
    nodes = [
        ("目标设定", "定义问题与目标", BLUE_BG, BLUE),
        ("策略选择", "选择方法与路径", GOLD_BG, GOLD),
        ("过程监控", "检查偏离与调整", PEACH_BG, PEACH),
        ("结果评估", "判断产出质量", PURPLE_BG, PURPLE),
    ]
    modes = [
        ("H", "人类主导", "学习者保留关键决策权", BLUE_BG, BLUE),
        ("A", "AI输出实际占据", "采纳 AI 输出，缺少显式协商", PEACH_BG, PEACH),
        ("J", "共同协商", "多轮对话后共同确定", PURPLE_BG, PURPLE),
    ]
    x0, y0 = 90, 58
    left_w, col_w, row_h = 260, 360, 125
    body.append(rect(x0, y0, left_w, 92, "#f5f7fa", "#d6dee8", 16, 2))
    body.append(text(x0 + left_w // 2, y0 + 38, "编码单元", 21, TEXT, 750))
    body.append(text(x0 + left_w // 2, y0 + 66, "设计认知决策节点", 16, MUTED))
    for i, (code, title_, sub, fill, stroke) in enumerate(modes):
        x = x0 + left_w + i * col_w
        body.append(rect(x + 18, y0, col_w - 36, 92, fill, stroke, 16, 2.3))
        body.append(text(x + col_w // 2, y0 + 34, code, 29, stroke, 800))
        body.append(text(x + col_w // 2, y0 + 62, title_, 19, TEXT, 750))
        body.append(text(x + col_w // 2, y0 + 82, sub, 14, MUTED))

    cell_text = [
        ["学习者定义目标", "AI目标被直接采用", "协商目标与约束"],
        ["学习者选择路径", "沿用AI建议路径", "比较方案后选择"],
        ["学习者主动纠偏", "跟随AI输出推进", "共同检查并调整"],
        ["学习者独立评判", "接受AI评估标准", "共同评估产出"],
    ]
    for r, (node, sub, fill, stroke) in enumerate(nodes):
        y = y0 + 92 + r * row_h
        body.append(rect(x0, y + 12, left_w - 18, row_h - 24, fill, stroke, 16, 2))
        body.append(text(x0 + 28, y + 55, f"{r+1}. {node}", 21, stroke, 800, "start"))
        body.append(text(x0 + 28, y + 84, sub, 15, MUTED, 400, "start"))
        if r < 3:
            body.append(line(x0 + left_w // 2 - 10, y + row_h - 12, x0 + left_w // 2 - 10, y + row_h + 8, "#8c98a6", 2, "arrow"))
        for c in range(3):
            x = x0 + left_w + c * col_w
            body.append(rect(x + 18, y + 12, col_w - 36, row_h - 24, "white", "#d5dde7", 14, 1.8))
            body.append(text(x + col_w // 2, y + 58, cell_text[r][c], 20, TEXT, 750))
            body.append(text(x + col_w // 2, y + 88, ["决策权在人", "行为层面A", "双方推理纳入"][c], 14, MUTED))

    t_y = 720
    body.append(rect(120, t_y, 1360, 105, ROSE_BG, ROSE, 20, 2.4, "12 8"))
    body.append(text(170, t_y + 43, "T", 32, ROSE, 800, "start"))
    body.append(text(225, t_y + 42, "动态切换指标", 23, TEXT, 760, "start"))
    body.append(text(225, t_y + 73, "记录 H / A / J 在节点内或跨节点之间的切换频率与方向，不作为第四种并列状态", 18, TEXT, 500, "start"))
    body.append(path("M1035 775 C1085 730 1145 730 1195 775", ROSE, 2.5, "arrow", "7 6"))
    body.append(text(1050, 800, "H", 20, BLUE, 800))
    body.append(text(1115, 754, "A", 20, PEACH, 800))
    body.append(text(1195, 800, "J", 20, PURPLE, 800))
    return html_doc("fig_framework_matrix", svg_doc(w, h, "\n".join(body)), w, h), w, h


FIGURES = {
    "fig_research_framework": build_research_framework,
    "fig_literature_funnel": build_literature_funnel,
    "fig_theory_radar": build_theory_matrix,
    "fig_framework_matrix": build_framework_matrix,
}


def export_png(name: str, width: int, height: int, output_dir: Path) -> None:
    chrome = CHROME if CHROME.exists() else Path(shutil.which("google-chrome") or "")
    if not chrome.exists():
        raise RuntimeError("Google Chrome not found")
    html_path = output_dir / f"{name}.html"
    png_path = output_dir / f"{name}.png"
    cmd = [
        str(chrome),
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        f"--window-size={width},{height}",
        f"--screenshot={png_path}",
        f"file://{html_path}",
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=120)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build compact SCI paper figures.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for generated HTML and PNG files.",
    )
    args = parser.parse_args()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    for name, builder in FIGURES.items():
        html_text, width, height = builder()
        svg_text = extract_svg(html_text)
        (output_dir / f"{name}.html").write_text(html_text, encoding="utf-8")
        (output_dir / f"{name}.svg").write_text(svg_text, encoding="utf-8")
        export_png(name, width, height, output_dir)
        print(
            f"built {output_dir / (name + '.html')}, "
            f"{output_dir / (name + '.svg')} and {output_dir / (name + '.png')}"
        )


if __name__ == "__main__":
    main()
