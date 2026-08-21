# PRD: Personalized Hiking Route Recommendation & Planning (MVP)

**Status:** Draft · **Author:** Ruby Wu · **Last updated:** 2026-08-21 · **Reviewers:** TBD — see [Open Questions § Stakeholders](#8-open-questions)

> Source: `personalized_hiking_prd_input.md`. Several input sections were explicitly marked incomplete by the author (research evidence, metric baselines/targets, NFR targets, out-of-scope confirmation, stakeholders). Per the input's own generation instructions, this PRD does not invent content to fill those gaps — it carries them forward as open questions or flagged placeholders, tagged `[data]` / `[hunch]` / `[assumption]` where a claim's provenance matters.

---

## 1. Overview

### Problem Statement

Beginner hikers (登山新手) lack the experience to translate a route's physical demand, slope, technical difficulty, and terrain risk into a judgment of whether that route fits their own ability and constraints. A single "easy / moderate / hard" label doesn't give them enough to decide **which route is right for them**, and even after finding route information, they must interpret and assemble it themselves — adding effort to both route selection and pre-trip planning. *(No quantified baseline exists yet — Section 4 of the source input is unfilled; see [Open Questions](#8-open-questions).)*

### Proposed Solution

Build a **Find → Plan → Go** MVP experience: break route difficulty into beginner-legible dimensions, capture a user's Hiking Profile, recommend 3–5 candidate routes with an explained Route Fit, generate a Personalized Hiking Plan once a route is chosen (transportation/trailhead, route timeline, suggested time schedule, key points), and surface a Departure Checklist before the trip.

### Success Metrics

| Metric | Baseline (today) | Target | When measured |
|---|---|---|---|
| % of users who successfully select a route after receiving recommendations | Unknown / to be measured | To be defined after baseline measurement | TBD |
| Time from beginning route exploration to final route selection | Unknown / to be measured | To be defined after baseline measurement | TBD |
| % of generated Hiking Plans viewed before departure | Unknown / to be measured | To be defined after baseline measurement | TBD |
| **Guardrail:** % of users who report Route Fit explanations as misleading or inconsistent | Unknown / to be measured | Must not increase post-launch | TBD |

> These four are pulled from a larger candidate list in the source input (Section 10) as the closest fit to the template's Outcome/Adoption/Guardrail slots. **None have a baseline or an instrumented owner yet** — per the [success-metrics guide](.agents/skills/prd-template/references/success-metrics-guide.md), a target without a baseline is unfalsifiable, so Phase 1 of implementation must include instrumenting these before a launch review can score against them. Full candidate metric set:
>
> - **Outcome:** route-selection success rate; exploration→selection time; user-reported confidence in "I know whether this route fits me"; % of recommended routes added to a plan.
> - **Planning funnel:** % of selected routes that proceed to plan generation; % of plans viewed before departure; Departure Checklist completion/usage rate.
> - **Guardrail:** % reporting Route Fit as misleading/inconsistent; % of recommendations rejected for violating stated Profile constraints; % of users who leave the product to find missing core planning information.

---

## 2. Context & Background

**Why Now:** Not provided in the source input — no forcing event (competitive move, declining metric, expiring commitment) is documented. **[Open Question — Product/Business]**

**Strategic Alignment:** Not provided in the source input — no company/team objective is quoted. **[Open Question — Product/Business]**

**User Research Summary:** Not yet completed. The source input (Section 4) scaffolds three intended findings — route difficulty is hard to interpret, users need personalized route selection, planning information is fragmented — plus a journey-friction-points slot, but every finding, evidence figure, and source is marked `[待補]` (to be filled in). **No interview counts, journey-map scores, or analytics are available, and none are asserted here.** The P0 scope below is instead traceable to the input's own Problem Statement and to explicitly labeled assumptions (Section 13) — see the traceability note under [Requirements](#4-requirements).

---

## 3. User Stories & Use Cases

**US1 — Understand Route Difficulty**
As a beginner hiker, I want to understand a route's difficulty by specific dimensions, so that I can judge what parts of the route may be challenging for me.

Acceptance Criteria:
- [ ] Route difficulty is displayed across multiple dimensions, at minimum: physical demand, slope/gradient, technical requirement, terrain risk.
- [ ] A route is never shown with only a single aggregate "easy/moderate/hard" label and no dimension breakdown.
- [ ] Which additional dimensions (beyond the four named above) are required for MVP is **unresolved** — source input leaves "other beginner-relevant difficulty information" open. **[Open Question]**

**US2 — Build Hiking Profile**
As a beginner hiker, I want to describe my hiking experience, physical condition, time constraints, transportation options, terrain restrictions, and preferences, so that recommendations can reflect my actual situation.

Acceptance Criteria:
- [ ] Profile capture includes: hiking experience, physical condition, acceptable hiking duration, transportation method, terrain restrictions, personal preferences.
- [ ] Which fields are mandatory vs. optional, and whether the Profile persists across trips or is edited per-trip, are **unresolved**. **[Open Question]**

**US3 — Receive Personalized Recommendations**
As a beginner hiker, I want to receive 3–5 routes that match my profile and current needs, so that I do not need to manually evaluate a large number of routes.

Acceptance Criteria:
- [ ] Given a completed Profile and trip-specific input, the system returns between 3 and 5 candidate routes.
- [ ] Behavior when fewer than 3 routes satisfy the Profile's constraints is **unresolved** — not specified in the source input, and not invented here. **[Open Question]**
- [ ] Why 3–5 is the right range is stated in the source as an **[assumption]**, not a validated finding.

**US4 — Understand Route Fit**
As a beginner hiker, I want to know why a route is or is not suitable for me, so that I can trust the recommendation and make the final decision myself.

Acceptance Criteria:
- [ ] Each recommended route shows a Route Fit explanation covering: why it's recommended, which conditions matched, which did not, and why it might not be recommended.
- [ ] Whether Route Fit is expressed as a score, a level, free text, or a combination is **unresolved**. **[Open Question]**

**US5 — Generate Hiking Plan**
As a beginner hiker, I want to receive a personalized plan after selecting a route, so that I know how to turn the route choice into an executable hiking trip.

Acceptance Criteria:
- [ ] Selecting a route triggers generation of a Personalized Hiking Plan derived from that route and the user's Profile.
- [ ] The Plan includes, at minimum, the four sub-components in US6–US8 below plus transportation/trailhead information.

**US6 — Understand Route Timeline**
As a beginner hiker, I want to see the route broken into major segments with distance, time, and difficulty, so that I can understand how the trip will progress.

Acceptance Criteria:
- [ ] The Plan breaks the full route into major segments.
- [ ] Each segment displays distance, estimated time, and segment-level difficulty.

**US7 — Plan My Time**
As a beginner hiker, I want recommended departure, checkpoint, and descent times, so that I can organize the trip without having to estimate the entire schedule myself.

Acceptance Criteria:
- [ ] The Plan includes a suggested departure time, arrival times at key checkpoints, suggested rest points, and an estimated descent/finish time.
- [ ] How personalized this schedule is (e.g., adjusted by the user's stated physical condition vs. a generic pace) is **unresolved**. **[Open Question]**

**US8 — Prepare Before Departure**
As a beginner hiker, I want a departure checklist, so that I can confirm essential preparations before leaving.

Acceptance Criteria:
- [ ] A Departure Checklist is available before the trip, covering at minimum: gear, maps, transportation, and other necessary pre-departure items.
- [ ] The exact item list is **unresolved** — source input names categories, not items. **[Open Question]**

---

## 4. Requirements

### Traceability note

Per generation instruction #2, every P0 requirement below traces to one of: the Problem Statement (§3 of the source input), an explicitly labeled assumption (§13 of the source input), or a still-open research question (§14). None trace to cited user research, because none exists yet in the source material — this is itself flagged, not concealed.

### Functional Requirements

**Must-have (P0) — all items below are P0 in the source input; the input defines no P1/P2 tier for MVP.**

| Requirement | Traces to |
|---|---|
| System presents Route Difficulty Breakdown across multiple dimensions | Problem Statement — "single label doesn't convey actual challenge" |
| System creates and persists a Hiking Profile | Problem Statement — "lacks a way to describe own ability/constraints" |
| System returns 3–5 candidate routes based on Profile + trip-specific need | Problem Statement + `[assumption]` that 3–5 is the right choice-effort balance |
| Each recommended route displays a Route Fit | Problem Statement — "even with a recommendation, users need to know why" |
| Route Fit states recommend/not-recommend reasons | Same as above |
| On route selection, system generates a Personalized Hiking Plan | Problem Statement — "still need help turning a chosen route into an executable trip" |
| Hiking Plan includes transportation & trailhead info | Same, + `[assumption]` that Google Maps/external services suffice for MVP |
| Hiking Plan includes Route Timeline | Problem Statement — planning info is fragmented and needs assembling |
| Hiking Plan includes a suggested time schedule | Same |
| Hiking Plan includes Key Points (hardest segment, rest points, cautions) | Same |
| User can view a Departure Checklist before departure | Problem Statement — "no simple pre-departure confirmation flow" + `[assumption]` this is worth its build cost |

**Should-have (P1) / Nice-to-have (P2):** Not defined in the source input. Do not treat any item above as P1/P2-demotable without a scoping decision — see [Implementation Plan](#7-implementation-plan).

### Non-Functional Requirements

The source input (Section 11) names required NFR topics but supplies **no targets** — per generation instruction #3, none are invented here. Each needs an explicit target from Engineering/Product before build:

- Performance / page load time — no target set
- Recommendation response time — no target set
- Accessibility — no standard specified (e.g., WCAG level)
- Data privacy for Hiking Profile — no policy specified (Profile includes physical-condition data, which may warrant sensitive-data handling — flagged, not assumed)
- Availability of external map/transportation services — no SLA specified; MVP's transportation feature is itself dependent on an external service `[assumption]`
- Error and fallback behavior — undefined (e.g., what happens when route data is incomplete/conflicting, per Section 14's open questions)
- Mobile usability — no target specified
- Reliability of route and planning data — no target specified

---

## 5. Design & User Experience

- **Mocks/wireframes:** None provided in the source input.
- **Key user flows:** Find (understand difficulty → build Profile → get recommendations → evaluate Route Fit) → Plan (select route → receive generated Plan covering transportation, timeline, schedule, key points) → Go (review Departure Checklist).
- **Edge cases and error states:** Largely unresolved — the source input's own open questions surface several without resolving them: fewer than 3 routes match a Profile; route data is incomplete or conflicting; external map/transportation service is unavailable. These need explicit design decisions before build, not default/invented behavior.

---

## 6. Technical Considerations

- **Recommendation engine architecture:** Whether Personalized Route Recommendation is rule-based, AI-based, or hybrid is an open question in the source input (Section 14) — not decided here.
- **Route Fit calculation:** How Route Fit is computed is likewise unresolved.
- **Dependencies:** MVP is expected to integrate Google Maps or another external map/transportation service for trailhead and transportation info — this is an explicit `[assumption]` in the source input, not a confirmed technical decision.
- **Data sourcing:** What route data source supplies difficulty dimensions (slope, terrain, technical difficulty, risk), transportation/trailhead info, and Route Timeline data is unresolved (Section 14, "Data/Technical").
- **Risks:** Route data availability/quality is a load-bearing unknown — nearly every P0 feature (difficulty breakdown, recommendations, Route Fit, timeline) depends on data that has no confirmed source yet.

---

## 7. Implementation Plan

- **Phase 1 (MVP):** All eleven P0 functional requirements listed in §4 — the full Find → Plan → Go experience. The source input does not tier these further.
- **Phase 2 / Phase 3:** Not defined in the source input. Per generation instruction #5 and #8, no future-phase content is invented here. The source input's Section 12 (Out of Scope) names items explicitly excluded from this MVP and marks its own status as "Needs confirmation": real-time GPS navigation, emergency rescue/SOS, hiking social network, community posting, equipment marketplace/e-commerce, real-time location sharing, advanced training/fitness tracking. No re-entry conditions for these are specified.

---

## 8. Open Questions

Carried directly from the source input (Section 14), organized by owner, plus the incomplete-status sections flagged elsewhere in this PRD. None have an assigned owner or deadline in the source material — that assignment itself is an open item.

**Product**
- Which Hiking Profile fields are mandatory vs. optional?
- Should Hiking Profile persist, or be editable per trip?
- What defines Route Fit — and is it a score, level, text, or combination?
- Why are 3–5 recommendations optimal?
- Which Route Difficulty dimensions are required for MVP (beyond the four named in US1)?
- How personalized should the Suggested Time Schedule be?
- Which items belong in the Departure Checklist?

**Research**
- Which journey step has the highest friction, per interview evidence? *(no evidence collected yet — Section 4)*
- Which P0 features address validated pain points vs. rest on assumption?
- What evidence supports that users want recommendation explanations?
- What evidence supports that planning-information fragmentation is a significant pain point?

**Data / Technical**
- What route data is available for the difficulty breakdown?
- How are slope, terrain, technical difficulty, and risk calculated or sourced?
- What data source supplies transportation and trailhead information?
- What data is required to generate Route Timeline?
- Is Personalized Route Recommendation rule-based, AI-based, or hybrid?
- How is Route Fit calculated?
- What happens when route data is incomplete or conflicting?

**Process / Governance (surfaced by this PRD, not the source's Section 14 list)**
- Success metric baselines and targets are unset — who owns instrumenting them, and by when?
- Why Now / Strategic Alignment are unstated — needed before prioritization against other initiatives.
- Stakeholders (Section 15) are only suggested by category (PM, Design, FE, BE, Data/AI Eng if ML-based recommendation, hiking-safety domain expert, business stakeholder, legal/privacy reviewer if required) — no names assigned, no reviewers confirmed.
- Out of Scope (Section 12) is marked "needs confirmation" — not yet approved as final.

---

## 9. Appendix

- Source input: `personalized_hiking_prd_input.md`
- Template and rubric: `.agents/skills/prd-template/SKILL.md`
- Success-metrics calibration: `.agents/skills/prd-template/references/success-metrics-guide.md`
- No competitive analysis or additional research links were provided in the source input.

---

## Self-Score (0–40 rubric, per skill instructions)

| Dimension | Score | Why |
|---|---|---|
| Problem grounding | 5 / 10 | Problem is user-framed and specific, but has zero cited research or quantified current-state data — Section 4 of the source is entirely unfilled. |
| Requirement testability | 7 / 10 | P0 requirements and acceptance criteria are concrete and traceable, but several NFRs are boilerplate topics with no thresholds, and some ACs still hinge on unresolved open questions. |
| Metric rigor | 3 / 10 | Metric *set* is reasonable (covers outcome, adoption, and guardrail), but **no metric has a baseline or target** — this is the PRD's biggest gap. |
| Scope & risk honesty | 8 / 10 | MVP scope is clearly bounded to P0 items, out-of-scope items are recorded (though unconfirmed), and open questions are extensive — but they carry no owner or deadline yet. |

**Total: 23 / 40** — below the 32+ ship-quality bar. The two biggest levers to close the gap: (1) complete Section 4 research so the problem statement can be quantified, and (2) instrument and baseline the success metrics before the next draft. Both are already logged as open questions above.
