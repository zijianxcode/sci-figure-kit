# Implementation Plan: Paper Index Landing Page

**Branch**: `001-paper-index` | **Date**: 2026-05-14 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `specs/001-paper-index/spec.md`

## Summary

Add a single static HTML page (`index.html`) at the project root that auto-discovers all papers in the `papers/` directory and renders them as a responsive card grid. Each card shows title, authors, venue, year, description, and thumbnail. Cards link to their respective `final.html` detail pages. Mobile-first, 390px baseline, using vanilla HTML/CSS/JS consistent with existing project conventions.

## Technical Context

**Language/Version**: HTML5, CSS3, vanilla JavaScript (ES6+)
**Primary Dependencies**: None (zero dependencies, consistent with project convention)
**Storage**: `meta.json` files in each paper directory + file system directory scanning (at build time via script)
**Testing**: Manual visual verification on mobile viewport (390px) and desktop
**Target Platform**: Modern browsers (Safari 15+, Chrome 90+, Firefox 90+), mobile-first
**Project Type**: Static site page
**Performance Goals**: Page load + render < 3s on 4G for up to 20 papers
**Constraints**: Zero runtime dependencies, single self-contained HTML file, all assets local
**Scale/Scope**: Initially ~1-5 papers, designed for up to 50

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Content-First Design | PASS | Card layout prioritizes paper information clarity over decoration |
| II. Mobile-Native | PASS | 390px baseline, card grid adapts upward for desktop |
| III. Academic Integrity | PASS | Metadata comes from structured meta.json per paper, no generated exaggeration |
| IV. Anti-AI-Flavor Writing | PASS | Page copy is minimal (heading, empty state message); paper content lives in detail pages |
| V. Progressive Refinement | PASS | Plan → tasks → implement with user review gates |
| VI. Shareability | PASS | Single self-contained HTML file, no external dependencies |

## Project Structure

### Documentation (this feature)

```text
specs/001-paper-index/
├── spec.md
├── plan.md              # This file
├── research.md
├── data-model.md
├── quickstart.md
└── checklists/
    └── requirements.md
```

### Source Code (repository root)

```text
index.html               # NEW: Landing page (single self-contained file)
papers/
├── attention-is-all-you-need/
│   ├── meta.json        # NEW: Paper metadata file
│   ├── draft.md
│   ├── final.html
│   ├── page-1.png
│   ├── page-2.png
│   └── page-3.png
└── [future-paper]/
    └── ...
scripts/
└── discover-papers.sh   # NEW: Script to generate paper manifest from directory scan
```

**Structure Decision**: Single static HTML file at project root (`index.html`). No build step, no framework, no JavaScript modules. A small shell script (`discover-papers.sh`) scans `papers/` directories and generates a JSON manifest that `index.html` loads. This keeps the HTML file self-contained with zero runtime dependencies while avoiding hardcoded paper lists.

## Complexity Tracking

No violations. This is the simplest possible implementation: one HTML file + one small data-generation script.
