# PRD: Personalized Hiking Route Recommendation & Planning (MVP)

## 1. Overview

### Problem Statement
When researching and planning an unfamiliar trail, hiking novices lack the experience needed to translate a route's physical demands, gradient, technical requirements, and terrain risk into terms they can compare against their own fitness, time, and constraints. This leaves them unable to judge whether a given route is right for them, and — once a route is picked — how to actually execute the hike safely. Even when route information exists, it is scattered across sources and requires the user to interpret and assemble it themselves, adding friction and uncertainty to both the route-selection decision and pre-trip preparation. `[data — user interviews + journey mapping, Findings 1–3, see Appendix]`

### Proposed Solution
A three-stage Find → Plan → Go experience. **Find**: break trail difficulty into novice-legible dimensions, combine them with a saved Hiking Profile, and surface 3–5 personalized route recommendations with a transparent "Route Fit" explanation for each. **Plan**: once a route is selected, auto-generate a Personalized Hiking Plan covering transportation/trailhead, a segmented route timeline, a suggested time schedule, and key points. **Go**: before departure, surface a Departure Checklist to confirm the user hasn't missed critical safety preparation.

### Success Metrics
> **Status: candidate metrics only — no baseline or target defined yet.** Per source section 10, these must be validated and baselined before they can gate a launch decision. Listed here as the current best candidates; see Open Questions.

*Primary Outcome*
- % of users who, after receiving recommendations, select a route
- Time from starting exploration to selecting a final route
- Self-reported confidence in "I know whether this route is right for me" (survey)
- % of recommended routes that get carried into hiking plan generation

*Planning*
- % of selected routes that go on to generate a Personalized Hiking Plan
- % of generated plans viewed again before departure
- Departure Checklist completion / usage rate

*Guardrail*
- % of users who find Route Fit reasoning misleading or inconsistent
- % of recommended routes rejected for violating the user's own stated Profile constraints
- % of users who leave the product to find core planning info elsewhere

`[gap]` No current baseline exists for any metric (source: section 10, "目前基準值：未知／待量測"). Per the prd-template skill's phase-2 gate, this PRD cannot claim a metric is "baselined" — it is carried forward as an explicit open item.

## 2. Context & Background

### Why Now
`[gap]` The source material does not include a business trigger, competitive event, or timing rationale for why this should be built now. Not fabricated here — see Open Questions.

### Strategic Alignment
`[gap]` No company objective or OKR was provided in the source material to align this PRD against. See Open Questions.

### User Research Summary
Two rounds of user interviews were completed, focused on (1) personalized route recommendation and (2) personalized hiking-plan generation, with hiking novices ("unfamiliar with route knowledge, but motivated to hike") as the interview population. `[data]`

**Finding 1 — Route difficulty is hard to interpret.** Novices can't tell whether a route labeled "easy" or "beginner-friendly" actually matches their fitness and experience, because everyone defines "easy" differently — and distance/time/elevation-gain numbers don't translate into "will this exhaust me." Users wanted specifics: stair count, sustained climbs, slippery surfaces, rope-assisted sections, which segment is hardest, and whether the descent will stress their knees. *(Source: personalized-route-recommendation interviews; journey map — "comparing whether a route fits me" stage)*

**Finding 2 — Users need personalized route selection, not just popular/beginner lists.** Users weigh whether a route is well-trodden by beginners, completable in 2–4 hours, easy to reach, scenic, and currently in good condition — but what they actually want to know is "can a novice like me finish this." Stated fears: running out of energy mid-route, the descent hurting more than the ascent, inaccurate time estimates, and not knowing where to rest or bail out. Users expect AI recommendations to include a personalized fitness assessment, a stated reason, a beginner-suitability read, difficulty callouts, alternatives, and supporting data. *(Source: personalized-route-recommendation interviews; AI-recommendation-trust interviews; journey map — "deciding whether to pick this route" stage)*

**Finding 3 — Planning information is fragmented.** Pre-trip planning info is scattered across blogs, YouTube, Instagram, Google Maps reviews, friend recommendations, hiking forums, official notices, and weather apps — inconsistent formats, some content stale enough that users can't tell if it's still valid. After picking a route, users still need to confirm route details, transportation, recent trail conditions, weather, gear/supplies, map screenshots, and departure/return times; unclear weather, trail conditions, transport, timing, difficulty, gear, or contingency plans make users reluctant to actually go. *(Source: both interview sets; journey map — "gathering candidate routes," "checking weather/conditions/safety," "final pre-departure check" stages)*

**Journey friction points.** The lowest-scoring steps are "comparing whether a route fits me" and "making the final go/no-go call" — the moments requiring the most judgment under the most uncertainty and psychological pressure. Users have access to distance, time, elevation, photos, reviews, and weather, but struggle to convert that data into "can I finish this," "is today a go," "when do I need to turn back," "how much water to bring," or "what do I do if weather or energy turns." *(Source: journey map friction analysis)*

Related opportunity areas identified in research: personalized route-fit judgment; difficulty translation into novice-legible terms; weather/conditions turned into an explicit go/reschedule/no-go call; automatic hiking-plan generation; and a pre-departure refresh of time-sensitive data. These map directly to the MVP scope in Section 4.

## 3. User Stories & Use Cases

### US1 — Understand route difficulty
As a **hiking novice**, I want to understand a route's challenge level through concrete difficulty dimensions, so that I can judge which segments will likely be hardest for me.

Acceptance Criteria:
- Each route displays a difficulty breakdown across 4 dimensions: Stamina, Steepness, Technical Trail, Sun Exposure (per Section 4 below)
- Each dimension shows a plain-language tier, not just a raw number (e.g., "sustained stairs — hard on knees")
- Breakdown is visible before the user commits to viewing full route details

### US2 — Build a hiking profile
As a **hiking novice**, I want to describe my experience, physical condition, time constraints, transportation, terrain limits, and preferences, so that recommended routes match my actual situation.

Acceptance Criteria:
- User can complete the 3 required fields (Duration Budget, Transportation Mode, Physical Condition) and any of the 3 optional fields (Hiking Experience, Terrain/Safety Constraints, Scenic Preferences)
- Profile is saved to the account and persists across sessions
- Profile auto-loads on every recommendation search
- User can temporarily override a field for a single search (e.g., "3 hours only today") without altering the saved baseline profile

### US3 — Get personalized route recommendations
As a **hiking novice**, I want to receive 3–5 routes matched to my Profile and current request, so that I don't have to manually evaluate a large list myself.

Acceptance Criteria:
- Recommendation set contains 3–5 routes, never more than 5
- Recommendations reflect both the saved Profile and any same-session overrides
- Set includes deliberate variety where possible (e.g., one easiest, one most scenic, one more challenging) `[assumption — see Section 9]`

### US4 — Understand route fit
As a **hiking novice**, I want to know why a route is or isn't a fit for me, so that I can trust the recommendation and make my own final call.

Acceptance Criteria:
- Each recommended route displays a Route Fit tier: "Highly Recommended," "Moderate Challenge," or "Not Recommended"
- Each route shows structured text listing both fit reasons (e.g., "direct public transit access") and caution points (e.g., "many stairs," "high sun exposure") — not a bare numeric score
- A route violating a hard constraint (unreachable by stated transport, exceeds time budget, exceeds the user's experience-based difficulty ceiling) is always shown as "Not Recommended," never as a soft-scored option

### US5 — Generate a hiking plan
As a **hiking novice**, I want a personalized hiking plan once I've picked a route, so that I know how to turn that choice into an executable trip.

Acceptance Criteria:
- Plan generation is triggered by selecting a recommended route
- Plan includes transportation/trailhead info, route timeline, suggested schedule, and key points (Section 4)
- Plan is saved and can be reopened before departure

### US6 — Understand the route timeline
As a **hiking novice**, I want the route broken into major segments with distance, time, and difficulty per segment, so that I understand how the full hike will unfold.

Acceptance Criteria:
- Timeline breaks the route into segments, each showing distance, estimated time, and segment-level difficulty
- Segments are presented in hiking order

### US7 — Plan trip timing
As a **hiking novice**, I want a suggested departure time, checkpoint times, and turnaround/descent time, so that I don't have to estimate the whole schedule myself.

Acceptance Criteria:
- Schedule applies a pace multiplier to base route time reflecting the user's stated fitness `[implementation approach — see Technical Considerations]`
- Schedule flags a latest-safe-turnaround time anchored to that day's sunset
- Schedule inserts rest breaks at regular intervals or key nodes

### US8 — Prepare before departure
As a **hiking novice**, I want a pre-departure checklist, so that I can confirm I haven't missed anything essential before leaving.

Acceptance Criteria:
- Checklist covers: map/GPX + offline map app, water/food with a route- and weather-specific quantity suggestion, gear (rain gear, non-slip footwear, backup headlamp), current trailhead weather and transit schedule, and sharing the plan with an emergency contact
- User can mark items complete
- Checklist is reachable from the saved hiking plan

## 4. Requirements

### Functional Requirements — P0 (MVP)

All items below are P0; the source material does not define a P1/P2 tier for this MVP — everything not listed here is explicitly Out of Scope (Section 7) rather than a lower-priority in-scope item.

**Find**
1. **Route Difficulty Breakdown** — traces to: US1, Finding 1. Present difficulty across 4 dimensions: Stamina (based on distance + elevation gain), Steepness (flat / sustained stairs / steep climb), Technical Trail (loose rock, mud/slippery, hands-required/rope sections), Sun Exposure (shaded / partial / fully exposed).
2. **Hiking Profile** — traces to: US2, Finding 2, `[assumption]` (Section 9). Required fields: Duration Budget, Transportation Mode, Physical Condition. Optional fields: Hiking Experience, Terrain/Safety Constraints, Scenic Preferences. Persisted to account; auto-loaded per search; per-search overrides do not overwrite the saved baseline.
3. **Personalized Route Recommendation** — traces to: US3, Finding 2, `[assumption]` (Section 9: 3–5 balances choice against decision fatigue). Return 3–5 candidate routes per search.
4. **Route Fit** — traces to: US4, Finding 1, Finding 2. Every recommended route carries a Route Fit tier (Highly Recommended / Moderate Challenge / Not Recommended) plus structured reasons-for and caution-points text. Hard constraints (transport unreachable, time budget exceeded, difficulty beyond the user's experience ceiling) force "Not Recommended" — never soft-scored around.

**Plan**
5. **Personalized Hiking Plan** — traces to: US5, Finding 3. Generated automatically once a route is selected, combining the route with the user's Profile.
6. **Transportation & Trailhead** — traces to: US5, US6, Finding 3. Shows transportation to the trailhead, trailhead location, and required entry/arrival info. `[implementation note]` MVP may integrate Google Maps or another external map/transit service — this is an implementation approach, not a committed product requirement (per generation rule 8).
7. **Route Timeline** — traces to: US6, Finding 3. Breaks the full route into segments, each showing distance, estimated time, and segment difficulty.
8. **Suggested Time Schedule** — traces to: US7, Finding 3. Provides a personalized schedule combining a fitness-based pace adjustment, a sunset-anchored latest-safe-turnaround time, and scheduled rest breaks. `[implementation note]` The specific pace-multiplier range and rest-interval cadence described in the source's Technical & Data Considerations (Section 6 below) are implementation approach, not settled product requirements, per generation rule 8 — the product requirement is that a personalized, safety-anchored schedule exists, not the specific multiplier value.
9. **Key Points** — traces to: US6, Finding 1, Finding 3. Flags the hardest segment, main rest points, and segments needing extra caution.

**Go**
10. **Departure Checklist** — traces to: US8, Finding 3, `[assumption]` (Section 9). Covers map/offline navigation, water/food quantity suggestion, gear, live trailhead weather/transit confirmation, and sharing the plan with an emergency contact.

### Non-Functional Requirements
> **Status: not yet defined — to be set jointly with Engineering/Product.** `[gap]` Source section 11 names the following categories with no targets. Listed here as scope markers only; none of these should be read as a committed SLA until targets are set.
- Performance / page load time
- Route-recommendation response time
- Accessibility
- Hiking Profile data privacy
- External map/transit service availability
- Error handling and fallback behavior
- Mobile usage experience
- Reliability of route and hiking-plan data

## 5. Design & User Experience
`[gap]` No mocks or wireframes were provided in the source material — none are linked here.

**Key user flow (derived from Find → Plan → Go scope, source Section 6):**
1. User completes/loads Hiking Profile → optionally overrides for this search
2. User receives 3–5 recommended routes, each with a Route Fit tier and reasoning
3. User selects a route → Personalized Hiking Plan is generated (transport, timeline, schedule, key points)
4. Before departure, user opens the Departure Checklist and confirms readiness

**Edge cases / error states named in source material** (source Section 12, "Data Conflict & Conservative Principle"):
- When weather or trail-condition data sources conflict, the product always surfaces the more conservative safety warning.
- Plans display a "data last updated" timestamp so users can judge whether information may be stale.
- Trust hierarchy for conflicting data: official safety/closure notices > active-week community GPX conditions > historical baseline data > general blogs/travel logs.

No other edge cases (e.g., no-connectivity behavior, empty recommendation results, profile-vs-route total mismatch) are specified in the source — flagged as an open design question in Section 8.

## 6. Technical Considerations
`[implementation approach as described in source — not restated as product requirements, per generation rule 8]`

**Data sources**
- Difficulty breakdown & trail tagging: government open data (Forestry Agency, county/city open data) for distance/elevation baselines; community GPX tracks for elevation profile and average pace; NLP/LLM extraction of terrain keywords ("rope," "loose rock," "stairs") from community text (Google Maps reviews, hiking-note posts).
- Transportation & trailhead: public transit via Taiwan's TDX platform or Google Directions API; trailhead location from government trail open data or OSM nodes; parking info from Google Maps Place API + review analysis.
- Risk & live weather: Central Weather Administration forecast API, Soil and Water Conservation Agency debris-flow warnings, Forestry Agency trail-closure notices.

**Personalization / fit model**
- Hybrid approach: stage 1 rule-based hard filtering (transport, time budget, safety-difficulty threshold); stage 2 fit-score ranking plus LLM-generated Route Fit explanation text.
- Route Fit scoring: weighted (time fit, stamina fit, transport fit, preference fit) with a hard veto (e.g., difficulty ≥2 tiers above the user's experience level auto-classifies as "Not Recommended").
- Route Timeline estimation: Naismith's Rule as the base pace model, adjusted by the user's Profile-derived pace multiplier.

**Data conflict handling**
- Trust hierarchy and conservative-fallback principle as described in Section 5 above.

**Dependencies & risk**
- MVP relies on multiple external data sources (government open data, TDX/Google APIs, weather APIs) of unverified completeness/reliability for this use case — `[assumption]`, see Section 9.
- LLM-generated Route Fit text and terrain-tag extraction quality directly affects the trust-building goal of US4 — no accuracy/quality bar has been set (see Open Questions).

## 7. Implementation Plan

### Phase 1 (MVP)
All 10 P0 items in Section 4, spanning Find, Plan, and Go, as scoped in source Section 7. Rationale: this is the minimum end-to-end path from "which route fits me" through "how do I execute it" through "am I ready to leave" that the research (Findings 1–3, Journey Friction Points) identified as the core gap.

### Phase 2 / Future Enhancements
> **Status: not committed — needs confirmation before being treated as roadmap, per source Section 13.**

The following are explicitly named as **out of scope for this MVP**, and should stay out unless separately confirmed and approved:
- Real-time GPS navigation
- Emergency/SOS
- Hiking social network / community posting features
- Gear marketplace / e-commerce
- Live location sharing
- Advanced training / fitness tracking
- Anything not directly required by the Find → Plan → Go MVP

Re-entry condition: none specified in source — should be defined by Product before any of the above is scheduled.

## 8. Open Questions
> Per generation rule 7, all of the following are surfaced rather than silently decided. None have an owner or deadline in the source material — both are marked TBD rather than invented.

| # | Question | Why it matters | Owner | Deadline | Cost of leaving unanswered |
|---|---|---|---|---|---|
| 1 | What is the current baseline for each candidate success metric (Section 1)? | Can't tell if MVP moved the needle without one | TBD | TBD | Ships without a way to prove impact |
| 2 | What are the target values for each success metric once baselined? | Needed to define "success" for this MVP | TBD | TBD | No launch/kill criteria |
| 3 | What are the NFR targets (performance, accessibility, privacy, reliability, fallback behavior)? | Currently only categories are named, no thresholds | TBD (Eng + Product) | TBD | Engineering can't build to a spec; accessibility/privacy risk goes unmanaged |
| 4 | Is the Out-of-Scope list (Section 7) final, or does anything on it need to move into MVP? | Currently marked "needs confirmation" in source | TBD | TBD | Scope could silently expand, or a needed feature could stay excluded |
| 5 | Who are the confirmed stakeholders (source lists only suggested roles: PM, UX, FE, BE, Data/AI Eng, hiking-safety domain expert, business stakeholder, legal/privacy)? | No named reviewers/approvers yet | TBD | TBD | No clear sign-off path, especially for safety-sensitive content |
| 6 | What is the business/strategic "why now" and OKR alignment for this initiative? | Not present in source material at all | TBD | TBD | Can't prioritize this against other initiatives |
| 7 | What accuracy/quality bar applies to LLM-generated Route Fit text and terrain-tag extraction? | Directly affects the trust goal in US4; a wrong or misleading Route Fit is also a named guardrail metric | TBD | TBD | Risk of shipping a feature that erodes trust instead of building it |
| 8 | What happens on no/low-connectivity in the field, or when zero routes match a Profile? | Not addressed in source material | TBD | TBD | Undefined behavior at points of highest user risk (mid-hike, no matches) |
| 9 | Will users actually trust and follow the recommended turnaround time in the field? | Flagged as `[assumption]` in source Section 14 — safety-relevant if false | TBD | TBD | Core safety mechanism (Suggested Time Schedule) may not change real behavior |

## 9. Appendix

### Assumptions carried from source (Section 14), all unvalidated
- `[assumption]` Users will provide enough Hiking Profile information to support personalization.
- `[assumption]` Breaking difficulty into multiple concrete dimensions makes it easier for novices to understand.
- `[assumption]` Showing Route Fit reasoning increases trust in recommendations.
- `[assumption]` 3–5 recommended routes balances choice against decision fatigue.
- `[assumption]` Users want the system to generate a hiking plan after route selection.
- `[assumption]` External services like Google Maps can supply sufficient transport/trailhead data for MVP.
- `[assumption]` A Departure Checklist delivers value proportionate to its build cost.
- `[assumption]` Users will trust and actually follow the system's suggested turnaround time in the field.
- `[assumption]` A simple Departure Checklist reduces novice gear-forgetting rather than being ignored as UI clutter.

### Research sources referenced in source material
- Interview — Personalized Route Recommendation interview notes
- Interview — AI Route Recommendation Trust interview notes
- Interview — Personalized Hiking Plan interview notes
- Journey Map — route-comparison, weather/condition-check, and final pre-departure stages

### Related documents
- Source input: `personalized_hiking_prd_input.md` (this repository)
