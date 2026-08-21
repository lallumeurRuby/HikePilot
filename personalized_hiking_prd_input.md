# PRD Input — Personalized Hiking Route Recommendation & Planning MVP

## 1. Feature / Product Name

**Personalized Hiking Route Recommendation & Planning**

產品涵蓋三個主要階段：

- **Find**：協助登山新手理解路線難度、建立個人登山 Profile，並取得個人化路線推薦。
- **Plan**：在選定路線後，產生可執行的個人化登山規劃。
- **Go**：在實際出發前，協助使用者完成必要的行前確認。

---

## 2. Target User

**Primary User:** 登山新手

### User Characteristics

- 缺乏足夠經驗判斷一條路線是否適合自己。
- 需要以容易理解的方式認識路線難度，而不是只看到單一「簡單 / 中等 / 困難」標籤。
- 會考量自身體力、可接受登山時間、交通方式、地形限制與個人偏好。
- 在選定路線後，仍需要協助安排交通、時間、路段與行前準備。

---

## 3. User Problem

### Problem Statement

登山新手在尋找與規劃陌生登山路線時，缺乏足夠經驗將路線的體力需求、坡度、技術難度與地形風險，對照自己的能力與限制，因此難以判斷「哪條路線適合我」以及「選定後該如何完成這趟登山」。

即使使用者能找到路線資訊，資訊通常仍需要自行解讀與整合，增加路線決策與行前規劃的負擔。

### Problems to Solve

1. 使用者無法從抽象的路線難度快速理解實際挑戰。
2. 使用者缺乏一套可以描述自身登山能力與限制的 Profile。
3. 使用者不知道哪些路線適合自己的能力與當次需求。
4. 即使收到推薦，使用者仍需要知道「為什麼適合 / 不適合」才能建立信任。
5. 選定路線後，使用者仍需要自行整理交通、登山口、路段、時間與休息安排。
6. 出發前缺乏一個簡單的行前確認流程。

---

## 4. User Research / Evidence

> **Status: To be completed from user interviews and journey research.**

請補入已完成的使用者訪談、User Journey Map、Customer Journey Map 或其他研究證據。

### Suggested Evidence Structure

#### Finding 1 — Route difficulty is hard to interpret

- **Finding:** [待補]
- **Evidence:** [待補，例如：X/X 位受訪者表示難以判斷「中等難度」是否適合自己]
- **Source:** [Interview / Journey Map / Analytics]

#### Finding 2 — Users need personalized route selection

- **Finding:** [待補]
- **Evidence:** [待補]
- **Source:** [待補]

#### Finding 3 — Planning information is fragmented

- **Finding:** [待補]
- **Evidence:** [待補]
- **Source:** [待補]

#### Journey Friction Points

- **Lowest-scoring step:** [待補]
- **Why it hurts:** [待補]
- **Related opportunity:** [待補]

---

## 5. Opportunity

### Primary Opportunity

幫助登山新手把「自己的能力與需求」對照「路線的實際挑戰」，降低選擇陌生路線時的不確定性。

### Secondary Opportunity

在使用者選定路線後，將分散的交通、路段、時間與行前準備資訊整理成可直接執行的個人化登山規劃。

---

## 6. Proposed Solution

建立一套從 **Find → Plan → Go** 的 MVP 體驗：

1. 將路線難度拆解成新手容易理解的維度。
2. 建立使用者 Hiking Profile。
3. 根據 Profile 與當次需求推薦 3–5 條候選路線。
4. 顯示每條路線與使用者的 Route Fit，說明推薦與不推薦原因。
5. 使用者選定路線後，自動產生 Personalized Hiking Plan。
6. 規劃中整理交通、登山口、Route Timeline、建議時間安排與 Key Points。
7. 出發前提供 Departure Checklist。

---

## 7. MVP Scope

### Find

#### P0 — Route Difficulty Breakdown

**Description**

將單一抽象的路線難度拆分成較容易理解的多個維度，例如：

- 體力需求
- 坡度
- 技術需求
- 地形風險
- 其他與新手判斷相關的難度資訊

**User Value**

讓登山新手不只看到「簡單 / 中等 / 困難」，而是理解這條路實際會難在哪裡。

---

#### P0 — Hiking Profile

**Description**

蒐集與個人化推薦相關的使用者資訊，包括：

- 登山經驗
- 體力狀況
- 可接受登山時間
- 交通方式
- 地形限制
- 個人偏好

**User Value**

建立個人化推薦與 Route Fit 判斷所需的基礎資料。

---

#### P0 — Personalized Route Recommendation

**Description**

根據 Hiking Profile 與使用者當次需求，推薦 **3–5 條候選路線**。

**User Value**

直接回答使用者最核心的問題：

> 我這次應該去哪裡？

---

#### P0 — Route Fit

**Description**

顯示每條候選路線與使用者的適合程度，並說明：

- 為什麼推薦
- 哪些條件符合
- 哪些條件不符合
- 為什麼可能不推薦

**User Value**

建立使用者對推薦結果的理解與信任，避免只有結果、沒有理由。

---

### Plan

#### P0 — Personalized Hiking Plan

**Description**

使用者選定路線後，根據該路線與使用者 Profile 產生個人化登山規劃。

**User Value**

從「選到一條路」進一步協助使用者理解「要怎麼完成這趟登山」。

---

#### P0 — Transportation & Trailhead

**Description**

整理：

- 前往登山口的交通方式
- 登山口位置
- 必要的入口 / 抵達資訊

**MVP Implementation Note**

MVP 可先整合 Google Maps 或其他外部地圖 / 交通服務。

---

#### P0 — Route Timeline

**Description**

將完整路線拆解成主要路段，顯示：

- 路段
- 距離
- 預估時間
- 該路段難度

**User Value**

將抽象的完整路線轉換為可理解的分段行程。

---

#### P0 — Suggested Time Schedule

**Description**

根據路線與使用者狀況提供建議時間安排，包括：

- 建議出發時間
- 抵達重要節點時間
- 建議休息節點
- 預計下山時間

**User Value**

協助缺乏規劃經驗的新手建立可執行的時間安排。

---

#### P0 — Key Points

**Description**

在規劃中標示重要節點，例如：

- 最困難路段
- 主要休息點
- 需要特別留意的路段

**User Value**

協助使用者進行體力分配與心理準備。

---

### Go

#### P0 — Departure Checklist

**Description**

在出發前提供簡單行前確認，包括：

- 裝備
- 地圖
- 交通
- 其他必要行前事項

**User Value**

降低因遺漏基本準備而影響登山行程的風險。

---

## 8. Functional Requirements

### P0 Requirements

- 系統需能呈現 Route Difficulty Breakdown。
- 系統需能建立並保存 Hiking Profile。
- 系統需根據 Profile 與當次需求提供 3–5 條候選路線。
- 每條推薦路線需顯示 Route Fit。
- Route Fit 必須提供推薦或不推薦原因。
- 使用者選定路線後，系統需能產生 Personalized Hiking Plan。
- Hiking Plan 需包含交通與登山口資訊。
- Hiking Plan 需包含 Route Timeline。
- Hiking Plan 需包含建議時間安排。
- Hiking Plan 需包含 Key Points。
- 使用者出發前需可查看 Departure Checklist。

---

## 9. User Stories

### US1 — Understand Route Difficulty

As a **beginner hiker**, I want to understand a route's difficulty by specific dimensions, so that I can judge what parts of the route may be challenging for me.

### US2 — Build Hiking Profile

As a **beginner hiker**, I want to describe my hiking experience, physical condition, time constraints, transportation options, terrain restrictions, and preferences, so that recommendations can reflect my actual situation.

### US3 — Receive Personalized Recommendations

As a **beginner hiker**, I want to receive 3–5 routes that match my profile and current needs, so that I do not need to manually evaluate a large number of routes.

### US4 — Understand Route Fit

As a **beginner hiker**, I want to know why a route is or is not suitable for me, so that I can trust the recommendation and make the final decision myself.

### US5 — Generate Hiking Plan

As a **beginner hiker**, I want to receive a personalized plan after selecting a route, so that I know how to turn the route choice into an executable hiking trip.

### US6 — Understand Route Timeline

As a **beginner hiker**, I want to see the route broken into major segments with distance, time, and difficulty, so that I can understand how the trip will progress.

### US7 — Plan My Time

As a **beginner hiker**, I want recommended departure, checkpoint, and descent times, so that I can organize the trip without having to estimate the entire schedule myself.

### US8 — Prepare Before Departure

As a **beginner hiker**, I want a departure checklist, so that I can confirm essential preparations before leaving.

---

## 10. Success Metrics

> **Status: Baseline and targets not yet defined.**

The following metrics are candidates and should be validated before finalizing the PRD.

### Primary Outcome Metrics

- Percentage of users who successfully select a route after receiving recommendations.
- Time from beginning route exploration to final route selection.
- User-reported confidence in answering: **「我知道這條路線是否適合我。」**
- Percentage of recommended routes that are added to a hiking plan.

### Planning Metrics

- Percentage of selected routes that proceed to Personalized Hiking Plan generation.
- Percentage of generated plans viewed before departure.
- Completion / usage rate of Departure Checklist.

### Guardrail Metrics

- Percentage of users who report that Route Fit explanations are misleading or inconsistent.
- Percentage of recommendations rejected because they violate stated Profile constraints.
- Percentage of users who need to leave the product to find missing core planning information.

### Baseline

- Current baseline: **Unknown / To be measured**

### Target

- Target values: **To be defined after baseline measurement**

---

## 11. Non-Functional Requirements

> **Status: To be defined with Engineering / Product.**

Topics that require explicit targets:

- Performance / loading time
- Recommendation response time
- Accessibility
- Data privacy for Hiking Profile
- Availability of external map / transportation services
- Error and fallback behaviour
- Mobile usability
- Reliability of route and planning data

---

## 12. Out of Scope

> **Status: Needs confirmation.**

The following items are not included in the provided MVP feature list and should remain out of scope unless separately approved:

- Real-time GPS navigation
- Emergency rescue / SOS
- Hiking social network
- Community posting
- Equipment marketplace / e-commerce
- Real-time location sharing
- Advanced training / fitness tracking
- Other features not directly required by Find → Plan → Go MVP

---

## 13. Assumptions

The following are currently **assumptions**, not validated facts:

- Users are willing to provide enough Hiking Profile information for personalization.
- Breaking route difficulty into dimensions will improve new hikers' understanding.
- Showing Route Fit reasons will increase recommendation trust.
- Recommending 3–5 routes provides an appropriate balance between choice and decision effort.
- Users want a generated hiking plan after selecting a route.
- External services such as Google Maps can provide sufficient transportation / trailhead support for MVP.
- A Departure Checklist provides meaningful value relative to its implementation cost.

---

## 14. Open Questions

### Product

- Which Hiking Profile fields are mandatory vs optional?
- Should Hiking Profile be persistent, or editable for each trip?
- What defines Route Fit?
- Should Route Fit be a score, level, textual explanation, or combination?
- Why are 3–5 recommendations optimal?
- Which Route Difficulty dimensions are required for MVP?
- How personalized should Suggested Time Schedule be?
- Which items belong in Departure Checklist?

### Research

- Which journey step has the highest friction according to interview evidence?
- Which of the P0 features directly address validated pain points?
- Which features are based primarily on assumptions?
- What evidence shows users want recommendation explanations?
- What evidence shows planning information fragmentation is a significant pain point?

### Data / Technical

- What route data is available for difficulty breakdown?
- How will slope, terrain, technical difficulty, and risk be calculated or sourced?
- What data source supplies transportation and trailhead information?
- What data is required to generate Route Timeline?
- Is Personalized Route Recommendation rule-based, AI-based, or hybrid?
- How is Route Fit calculated?
- What happens when route data is incomplete or conflicting?

---

## 15. Stakeholders

> **Status: To be completed.**

Suggested stakeholder categories:

- Product Manager
- Product / UX Designer
- Frontend Engineer
- Backend Engineer
- Data / AI Engineer, if recommendation uses AI or ML
- Domain expert / hiking safety reviewer
- Business stakeholder
- Legal / Privacy reviewer, if required

---

## 16. PRD Generation Instruction

Use the information above to generate a PRD following the **PRD Template Skill**.

Requirements:

1. Keep the problem statement user-centered and solution-neutral.
2. Trace every P0 requirement back to a user problem, research finding, or clearly labeled assumption.
3. Do not invent research evidence, baselines, success targets, or technical constraints.
4. Clearly label unsupported claims as `[assumption]` or `[hunch]`.
5. Separate MVP scope from future enhancements.
6. Include acceptance criteria for each primary user story.
7. Surface unresolved questions explicitly rather than silently deciding them.
8. Do not convert implementation assumptions into settled product requirements.
