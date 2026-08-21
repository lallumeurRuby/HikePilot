# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **product management workspace**, not a software codebase. There is no application code, build system, linter, or test suite here — do not go looking for one. The repo currently holds PRD (Product Requirements Document) source material for **HikePilot**, a personalized hiking route recommendation and planning product, plus an installed Claude Code skill for generating PRDs.

## Repository structure

- `personalized_hiking_prd_input.md` — the raw PRD input for the "Personalized Hiking Route Recommendation & Planning" MVP, written largely in Traditional Chinese with English section headers. It follows a fixed structure (feature name, target user, problem statement, opportunity, MVP scope, functional requirements, user stories, success metrics, NFRs, out-of-scope, assumptions, open questions, stakeholders) and ends with an explicit **PRD Generation Instruction** section — this is the authoritative brief for producing the actual PRD.
- `.agents/skills/prd-template/` — an installed Claude Code skill (`prd-template`, pulled from `mohitagw15856/pm-claude-skills` per `skills-lock.json`) that defines the PRD template, writing guidelines, a scoring rubric, and a fill-in skeleton. Use this skill when asked to draft a PRD from `personalized_hiking_prd_input.md` or any similar input.
- `skills-lock.json` — lockfile recording the installed skill's source and content hash. Don't hand-edit; it's maintained by the skill installer.

## Working with the PRD input

The input file's rules 8 (`PRD Generation Instruction`) govern how any generated PRD must treat this source material — these are the load-bearing constraints:

1. Keep the problem statement user-centered and solution-neutral.
2. Trace every P0 requirement back to a user problem, research finding, or clearly labeled assumption.
3. Do not invent research evidence, baselines, success targets, or technical constraints.
4. Clearly label unsupported claims as `[assumption]` or `[hunch]`.
5. Separate MVP scope from future enhancements.
6. Include acceptance criteria for each primary user story.
7. Surface unresolved questions explicitly rather than silently deciding them.
8. Do not convert implementation assumptions into settled product requirements.

Note that the input file itself flags several sections as incomplete (`Status: To be completed`, `[待補]` placeholders) — Section 4 (User Research/Evidence), Section 10 (baselines/targets), Section 11 (NFR targets), Section 12 (Out of Scope confirmation), and Section 15 (Stakeholders). Do not fabricate content to fill these; preserve them as open gaps in any generated PRD, per instruction rules 3 and 7 above.

## Using the `prd-template` skill

The skill (`.agents/skills/prd-template/SKILL.md`) is self-contained and describes:

- A four-phase drafting loop: lock the problem statement → baseline the success metric → draft sections tracing up to the problem → hand off the success metric for downstream RICE prioritization.
- The required PRD section order (Overview, Context & Background, User Stories, Requirements, Design & UX, Technical Considerations, Implementation Plan, Open Questions, Appendix).
- A 0–40 scoring rubric (problem grounding, requirement testability, metric rigor, scope & risk honesty) — score generated PRDs against it; 32+ is considered ship-quality.
- `templates/prd-skeleton.md` for a blank fill-in-yourself PRD structure.
- `references/success-metrics-guide.md` for calibrating the success-metrics table (the four-part metric test: moves iff the feature works, has a baseline, has a deadline, someone reviews it).

The skill references an upstream `/assumption-mapper` step and a `professional-brain/` knowledge store and `docs/craft/product-decisions.md` glossary — neither exists in this repository, so treat those as not available here; work directly from `personalized_hiking_prd_input.md`.
