# Tasks: Paper Index Landing Page

**Input**: Design documents from `specs/001-paper-index/`
**Prerequisites**: plan.md, spec.md, data-model.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Data foundation — all user stories depend on paper metadata being available

- [ ] T001 [P] Create `meta.json` for the existing paper at `papers/attention-is-all-you-need/meta.json` with title, authors, year, venue, description, thumbnail, and detail_page fields per data-model.md
- [ ] T002 Create `scripts/discover-papers.sh` — scans `papers/` subdirectories, reads each `meta.json`, generates `papers/manifest.json` with paper entries sorted by year descending

---

## Phase 2: User Story 1 — Browse All Papers (Priority: P1)

**Goal**: Visitor sees a scrollable card grid with all papers

**Independent test**: Open `index.html` on 390px mobile viewport. Verify all papers appear as cards with title, first author, year, and thumbnail.

- [ ] T003 [US1] Create `index.html` at project root — single static HTML file with embedded CSS and JS, zero external dependencies
- [ ] T004 [US1] Implement card grid layout in `index.html` — mobile-first single-column layout (390px baseline), body text ≥ 16px per FR-005
- [ ] T005 [US1] Implement manifest loading in `index.html` — fetch `papers/manifest.json`, parse paper array, render cards dynamically
- [ ] T006 [US1] Implement paper card rendering — each card shows title, first author name, publication year, and thumbnail image per FR-002, FR-003
- [ ] T007 [US1] Handle empty state — when 0 papers, show brief message explaining the project (FR-007)
- [ ] T008 [US1] Handle missing thumbnail — generate a placeholder (CSS gradient or SVG) with paper title text when thumbnail file is absent (FR-006)

---

## Phase 3: User Story 2 — Navigate to Paper Detail (Priority: P1)

**Goal**: Tapping a card navigates to the paper's detail page

**Independent test**: From index page, tap a card. Verify navigation to correct `final.html`.

- [ ] T009 [US2] Add click/tap handler to each card in `index.html` — navigate to `papers/<id>/<detail_page>` per FR-004
- [ ] T010 [US2] Handle paper in draft status — when `detail_page` points to a non-final file, show visual indicator on card ("Draft" badge) and link to the available page

---

## Phase 4: User Story 3 — Rich Metadata Display (Priority: P2)

**Goal**: Cards show full metadata so visitors can evaluate papers without clicking

**Independent test**: Verify each card shows full title, author list with et al. truncation, venue, and description.

- [ ] T011 [US3] Implement author list with et al. truncation in `index.html` — show first 3 authors followed by "et al." if more than 3 (FR-008)
- [ ] T012 [US3] Display venue/journal name on card when available, gracefully omit when absent (FR-009)
- [ ] T013 [US3] Display one-line description on card, truncated to 2 lines with ellipsis if overflow

---

## Phase 5: Polish & Cross-Cutting

**Purpose**: Responsive layout, visual consistency

- [ ] T014 Implement responsive grid — switch from single column (mobile) to 2-column (≥768px) to 3-column (≥1024px) per FR-010
- [ ] T015 Apply paper-card visual design system — warm white background, deep blue-gray accents, serif headings + sans-serif body per constitution
- [ ] T016 Handle long title truncation — max 2 lines with ellipsis on card (edge case)

---

## Dependencies & Execution Order

```
Phase 1 (T001, T002) [parallel]
    │
    ▼
Phase 2 (T003 → T004 → T005 → T006 → T007, T008 [parallel])
    │
    ▼
Phase 3 (T009 → T010)
    │
    ▼
Phase 4 (T011, T012, T013 [parallel])
    │
    ▼
Phase 5 (T014, T015, T016 [parallel])
```

## Notes

- T001 and T002 can run in parallel (different files)
- T007 and T008 can run in parallel (different concerns within same file)
- T011, T012, T013 can run in parallel (different card sections)
- After Phase 2 is complete, the feature is already usable as MVP (P1 stories done)
