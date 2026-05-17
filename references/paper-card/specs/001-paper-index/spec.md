# Feature Specification: Paper Index Landing Page

**Feature Branch**: `001-paper-index`

**Created**: 2026-05-14

**Status**: Draft

**Input**: User description: "Add a paper index landing page that shows all processed papers as cards with title, authors, date, and thumbnail preview, so visitors can browse the collection."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Browse All Papers (Priority: P1)

A visitor opens the paper-card site and sees a scrollable grid of paper cards. Each card shows the paper title, first author name, publication year, and a thumbnail preview image. The visitor scans the collection at a glance and gets a clear sense of what papers are available.

**Why this priority**: This is the entire feature — without it there is no index page. Every other story builds on this.

**Independent Test**: Open the index page in a mobile browser (390px width). Verify that all papers in the `papers/` directory appear as cards with title, author, year, and thumbnail visible.

**Acceptance Scenarios**:

1. **Given** the project has 3 processed papers in `papers/`, **When** a visitor opens the index page, **Then** they see 3 cards arranged in a scrollable layout, each showing title, first author, year, and a thumbnail.
2. **Given** the project has only 1 paper, **When** a visitor opens the index page, **Then** they see a single card displayed prominently without awkward empty space.
3. **Given** the project has 0 papers (fresh setup), **When** a visitor opens the index page, **Then** they see a brief message explaining the project and how papers will appear here.

---

### User Story 2 - Navigate to Paper Detail (Priority: P1)

A visitor finds an interesting paper card, taps it, and is taken to that paper's full detail page (`final.html`) to read the complete analysis.

**Why this priority**: The index is a gateway — it must connect visitors to the full content. Without navigation, the index has no purpose.

**Independent Test**: From the index page, tap any paper card. Verify the browser navigates to the correct paper's `final.html`.

**Acceptance Scenarios**:

1. **Given** a paper card for "Attention Is All You Need", **When** the visitor taps the card, **Then** the browser opens `papers/attention-is-all-you-need/final.html`.
2. **Given** a paper card on the index page, **When** the visitor taps it, **Then** the transition feels responsive (page loads within acceptable mobile browsing time).

---

### User Story 3 - Paper Metadata Display (Priority: P2)

Each card displays rich metadata so visitors can evaluate a paper's relevance before clicking. Beyond basic info, the card shows the full author list (truncated with "et al." if more than 3), the venue/journal name, and a one-line description or key finding.

**Why this priority**: Metadata helps visitors decide which paper to read. Without it, they're clicking blindly. But the index still works with basic info from P1.

**Independent Test**: Verify each card shows: full title, author list (with et al. truncation), venue name, publication year, and a one-line description.

**Acceptance Scenarios**:

1. **Given** a paper with 2 authors, **When** the card renders, **Then** both author names are displayed.
2. **Given** a paper with 5 authors, **When** the card renders, **Then** the first 3 authors are shown followed by "et al.".
3. **Given** a paper without a venue field, **When** the card renders, **Then** the venue line is gracefully omitted rather than showing blank space.

---

### Edge Cases

- What happens when a paper directory exists but has no `final.html`? Show the card with metadata but mark it as "in progress" or link to the draft instead.
- What happens when a paper has no thumbnail image? Show a generated placeholder based on the paper title.
- What happens when paper title is very long (200+ characters)? Truncate to 2 lines with ellipsis on the card.
- What happens on desktop widths? Cards switch from single-column to a multi-column grid (max 3 columns) while keeping readable type sizes.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST automatically discover all paper directories under `papers/` and render a card for each one.
- **FR-002**: System MUST display paper title, first author name, and publication year on every card (minimum viable card).
- **FR-003**: System MUST display a thumbnail preview image for each paper when available.
- **FR-004**: System MUST link each card to the corresponding paper's detail page.
- **FR-005**: System MUST render correctly on 390px-width mobile viewport with body text ≥ 16px.
- **FR-006**: System MUST generate a placeholder thumbnail for papers that lack one.
- **FR-007**: System MUST handle 0, 1, and many papers gracefully in layout.
- **FR-008**: System MUST display author list with "et al." truncation after 3 authors.
- **FR-009**: System MUST display venue/journal name when available and gracefully omit it when not.
- **FR-010**: System MUST adapt layout from single-column (mobile) to multi-column grid (desktop, max 3 columns).

### Key Entities

- **Paper Card**: Represents one processed paper. Key attributes: title, authors (list), publication year, venue, thumbnail image path, detail page path, status (draft/final). Derived from scanning the `papers/` directory structure.
- **Index Page**: The container page that hosts all Paper Cards. Responsible for layout adaptation and empty-state messaging.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A visitor can identify all available papers and their topics within 10 seconds of loading the index page.
- **SC-002**: The index page loads and renders all cards in under 3 seconds on a 4G mobile connection with up to 20 papers.
- **SC-003**: On a 390px viewport, all card text is readable without zooming (≥ 16px body text).
- **SC-004**: A visitor can navigate from index to any paper detail page in a single tap.

## Assumptions

- The project already has a well-defined `papers/` directory structure (each paper in its own subdirectory with `final.html` and PNG files).
- Paper metadata (title, authors, year, venue, description) will be stored in a structured format within each paper directory. For v1, this can be a simple `meta.json` or frontmatter in the draft.
- The index page is a single static HTML file following the same technology approach as existing paper-card pages (vanilla HTML/CSS/JS, no framework).
- Mobile-first design with 390px baseline, consistent with paper-card's existing design system.
- Desktop support means responsive grid up to ~1200px max-width, not a separate desktop design.
