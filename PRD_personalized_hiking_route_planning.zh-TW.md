# PRD：個人化登山路線推薦與規劃（MVP）

**狀態：** 草稿 · **作者：** Ruby Wu · **最後更新：** 2026-08-21 · **審閱者：** 待定 — 詳見 [Open Questions § 利害關係人](#8-open-questions)

> 來源文件：`personalized_hiking_prd_input.md`。原始輸入文件中有多個章節被作者明確標註為尚未完成（研究證據、指標基準值／目標值、非功能需求目標、Out of Scope 確認、利害關係人名單）。依據原始輸入文件自身的 PRD 產出規範，本 PRD 不會捏造內容來補齊這些缺口，而是將其保留為 Open Questions 或明確標示的待補欄位，並在需要標明來源性質時加上 `[data]`／`[hunch]`／`[assumption]` 標籤。

---

## 1. Overview（總覽）

### Problem Statement（問題陳述）

登山新手（beginner hikers）缺乏足夠經驗，無法將一條路線的體力需求、坡度、技術難度與地形風險，轉換成「這條路線是否適合自己」的判斷。單一的「簡單／中等／困難」標籤，不足以讓他們決定**哪條路線適合自己**；即使找到了路線資訊，仍需要自行解讀與整合，這增加了路線選擇與行前規劃的負擔。*（目前尚無量化基準值——原始輸入文件第 4 節仍未填寫，詳見 [Open Questions](#8-open-questions)。）*

### Proposed Solution（提案方案）

打造一套 **Find → Plan → Go** 的 MVP 體驗：將路線難度拆解成新手容易理解的多個維度、建立使用者的 Hiking Profile、推薦 3–5 條候選路線並附上有說明的 Route Fit、在使用者選定路線後產生 Personalized Hiking Plan（交通／登山口、Route Timeline、建議時間安排、Key Points），並在出發前提供 Departure Checklist。

### Success Metrics（成功指標）

| 指標 | 現況基準值 | 目標值 | 衡量時機 |
|---|---|---|---|
| 使用者在收到推薦後成功選定路線的比例 | 未知／待測量 | 待基準值確認後再定義 | 待定 |
| 從開始探索路線到最終選定路線所需的時間 | 未知／待測量 | 待基準值確認後再定義 | 待定 |
| 已產生的 Hiking Plan 在出發前被查看的比例 | 未知／待測量 | 待基準值確認後再定義 | 待定 |
| **Guardrail：** 使用者回報 Route Fit 說明「令人誤解或前後不一致」的比例 | 未知／待測量 | 上線後不得上升 | 待定 |

> 以上四項是從原始輸入文件（第 10 節）較大的候選指標清單中，挑選出與範本中 Outcome／Adoption／Guardrail 欄位最相符的項目。**目前沒有任何一項有基準值或負責追蹤的窗口**——依據 [success-metrics 指南](.agents/skills/prd-template/references/success-metrics-guide.md)，沒有基準值的目標是無法被證偽的，因此 Phase 1 的實作範圍必須包含這些指標的埋點與量測，之後才能在上線檢視會議上據此評分。完整候選指標清單如下：
>
> - **Outcome（成果指標）：** 路線選定成功率；探索到選定的耗時；使用者對「我知道這條路線是否適合我」的自我評估信心；被加入規劃的推薦路線比例。
> - **Planning funnel（規劃漏斗指標）：** 已選定路線中進入 Plan 產生流程的比例；產生的 Plan 在出發前被查看的比例；Departure Checklist 的完成／使用率。
> - **Guardrail（防護指標）：** 回報 Route Fit 說明令人誤解或不一致的比例；因違反使用者 Profile 條件而被拒絕的推薦比例；需要離開產品才能找到核心規劃資訊的使用者比例。

---

## 2. Context & Background（背景脈絡）

**Why Now（為何是現在）：** 原始輸入文件未提供——沒有記載任何促成此案的事件（例如競品動作、指標下滑、合約到期等）。**［Open Question — Product/Business］**

**Strategic Alignment（策略對齊）：** 原始輸入文件未提供——沒有引用任何公司或團隊層級的目標。**［Open Question — Product/Business］**

**User Research Summary（使用者研究摘要）：** 尚未完成。原始輸入文件（第 4 節）雖然搭好了三個預期發現的骨架——路線難度不易理解、使用者需要個人化路線選擇、規劃資訊分散——並預留了 Journey Friction Points 欄位，但每一項 Finding、Evidence 與 Source 都標註為 `[待補]`。**目前沒有任何訪談人數、Journey Map 分數或分析數據可供引用，本文件也不會捏造這些內容。** 下方的 P0 範圍改為以原始輸入文件自身的 Problem Statement 與明確標註的 Assumptions（第 13 節）作為依據——詳見 [Requirements](#4-requirements) 章節下的可追溯性說明。

---

## 3. User Stories & Use Cases（使用者故事與使用情境）

**US1 — 理解路線難度（Understand Route Difficulty）**
身為一位登山新手，我希望能透過具體的維度來理解一條路線的難度，以便判斷路線中哪些部分可能對我構成挑戰。

驗收標準（Acceptance Criteria）：
- [ ] 路線難度以多個維度呈現，至少包含：體力需求、坡度／坡度變化、技術需求、地形風險。
- [ ] 任何路線都不會只顯示單一的「簡單／中等／困難」聚合標籤，而沒有維度拆解。
- [ ] 除上述四項之外，MVP 是否還需要其他難度維度**尚未定案**——原始輸入文件將「其他與新手判斷相關的難度資訊」列為開放項目。**［Open Question］**

**US2 — 建立 Hiking Profile（Build Hiking Profile）**
身為一位登山新手，我希望能描述自己的登山經驗、體力狀況、可接受的登山時間、交通方式、地形限制與個人偏好，以便推薦結果能反映我的實際狀況。

驗收標準：
- [ ] Profile 蒐集內容包含：登山經驗、體力狀況、可接受登山時間、交通方式、地形限制、個人偏好。
- [ ] 哪些欄位為必填、哪些為選填，以及 Profile 是否跨行程保留或需逐次編輯，**尚未定案**。**［Open Question］**

**US3 — 取得個人化推薦（Receive Personalized Recommendations）**
身為一位登山新手，我希望收到 3–5 條符合我 Profile 與當次需求的路線，以便不需要自己手動評估大量路線。

驗收標準：
- [ ] 在 Profile 與當次需求輸入完成後，系統回傳 3 至 5 條候選路線。
- [ ] 當符合 Profile 條件的路線少於 3 條時系統應如何處理，**尚未定案**——原始輸入文件未說明，本文件也不代為決定。**［Open Question］**
- [ ] 「為何 3–5 條是最適區間」在原始輸入文件中僅列為 **[assumption]**，並非已驗證的結論。

**US4 — 理解 Route Fit（Understand Route Fit）**
身為一位登山新手，我希望知道一條路線為何適合或不適合我，以便信任推薦結果並自行做出最終決定。

驗收標準：
- [ ] 每條推薦路線都顯示 Route Fit 說明，涵蓋：為何推薦、哪些條件符合、哪些條件不符合，以及為何可能不推薦。
- [ ] Route Fit 是以分數、等級、文字說明或組合方式呈現，**尚未定案**。**［Open Question］**

**US5 — 產生 Hiking Plan（Generate Hiking Plan）**
身為一位登山新手，我希望在選定路線後收到個人化規劃，以便知道如何把「選定路線」落實成一趟可執行的登山行程。

驗收標準：
- [ ] 選定路線後，系統會依據該路線與使用者 Profile 產生 Personalized Hiking Plan。
- [ ] Plan 內容至少包含下方 US6–US8 所列四項子項目，以及交通／登山口資訊。

**US6 — 理解 Route Timeline（Understand Route Timeline）**
身為一位登山新手，我希望看到路線被拆解成主要路段，並附上距離、時間與難度，以便理解整趟行程將如何進行。

驗收標準：
- [ ] Plan 會將完整路線拆解成主要路段。
- [ ] 每個路段顯示距離、預估時間，以及該路段的難度等級。

**US7 — 安排我的時間（Plan My Time）**
身為一位登山新手，我希望取得建議的出發、抵達節點與下山時間，以便不需要自己估算整趟行程的時間安排。

驗收標準：
- [ ] Plan 包含建議出發時間、抵達重要節點的時間、建議休息節點，以及預估下山／完成時間。
- [ ] 此時間安排的個人化程度（例如是否依使用者自述的體力狀況調整，而非採用通用配速）**尚未定案**。**［Open Question］**

**US8 — 出發前準備（Prepare Before Departure）**
身為一位登山新手，我希望有一份行前檢查清單，以便在出發前確認必要的準備事項。

驗收標準：
- [ ] 出發前可查看 Departure Checklist，內容至少涵蓋：裝備、地圖、交通與其他必要行前事項。
- [ ] 確切的項目清單**尚未定案**——原始輸入文件僅列出類別，未列出具體項目。**［Open Question］**

---

## 4. Requirements（需求）

### 可追溯性說明

依據 PRD 產出規範第 2 點，下方每一項 P0 需求都必須追溯至以下三者之一：Problem Statement（原始輸入文件第 3 節）、明確標註的 Assumption（原始輸入文件第 13 節），或仍未解決的研究性 Open Question（第 14 節）。沒有任何一項是依據已引用的使用者研究，因為原始素材中目前並不存在——這一點本身也被明確標示，而非隱藏。

### Functional Requirements（功能需求）

**Must-have（P0）——以下項目在原始輸入文件中皆為 P0；原始輸入文件並未為 MVP 定義 P1／P2 分級。**

| 需求 | 追溯依據 |
|---|---|
| 系統呈現 Route Difficulty Breakdown（多維度難度拆解） | Problem Statement ——「單一標籤無法傳達實際挑戰」 |
| 系統可建立並保存 Hiking Profile | Problem Statement ——「缺乏描述自身能力／限制的方式」 |
| 系統依 Profile 與當次需求回傳 3–5 條候選路線 | Problem Statement ＋ `[assumption]`：3–5 條是合適的選擇與決策負擔平衡點 |
| 每條推薦路線顯示 Route Fit | Problem Statement ——「即使收到推薦，使用者仍需要知道為什麼」 |
| Route Fit 需說明推薦／不推薦原因 | 同上 |
| 使用者選定路線後，系統產生 Personalized Hiking Plan | Problem Statement ——「仍需要協助把選定路線轉換成可執行行程」 |
| Hiking Plan 包含交通與登山口資訊 | 同上，＋ `[assumption]`：Google Maps／外部服務足以支援 MVP |
| Hiking Plan 包含 Route Timeline | Problem Statement ——規劃資訊分散，需要被整理 |
| Hiking Plan 包含建議時間安排 | 同上 |
| Hiking Plan 包含 Key Points（最難路段、主要休息點、注意事項） | 同上 |
| 使用者出發前可查看 Departure Checklist | Problem Statement ——「缺乏簡單的行前確認流程」＋ `[assumption]`：此功能的價值值得其開發成本 |

**Should-have（P1）／Nice-to-have（P2）：** 原始輸入文件未定義。在沒有明確的範圍決策（scoping decision）之前，不應將上述任一項目降級為 P1／P2——詳見 [Implementation Plan](#7-implementation-plan)。

### Non-Functional Requirements（非功能需求）

原始輸入文件（第 11 節）列出了需要定義目標值的 NFR 主題，但**並未提供任何目標值**——依據 PRD 產出規範第 3 點，本文件不會捏造目標值。以下每一項都需要工程／產品團隊在開發前明確訂出目標：

- 效能／頁面載入時間——尚未設定目標
- 推薦回應時間——尚未設定目標
- 無障礙（Accessibility）——尚未指定標準（例如 WCAG 等級）
- Hiking Profile 的資料隱私——尚未指定政策（Profile 包含體力狀況等資料，可能需要敏感資料處理機制——此處僅標示風險，不預設答案）
- 外部地圖／交通服務的可用性——尚未指定 SLA；MVP 的交通功能本身即依賴外部服務 `[assumption]`
- 錯誤與 fallback 行為——尚未定義（例如路線資料不完整或衝突時該如何處理，對應第 14 節的 Open Questions）
- 行動裝置可用性——尚未指定目標
- 路線與規劃資料的可靠性——尚未指定目標

---

## 5. Design & User Experience（設計與使用者體驗）

- **設計稿／線框圖：** 原始輸入文件未提供。
- **主要使用者流程：** Find（理解難度 → 建立 Profile → 取得推薦 → 評估 Route Fit）→ Plan（選定路線 → 取得涵蓋交通、Timeline、時間安排、Key Points 的 Plan）→ Go（查看 Departure Checklist）。
- **邊界情境與錯誤狀態：** 大多尚未定案——原始輸入文件自身的 Open Questions 已點出多個未解決的情境：符合 Profile 的路線少於 3 條、路線資料不完整或衝突、外部地圖／交通服務無法使用。這些都需要在開發前有明確的設計決策，而不是預設或捏造的行為。

---

## 6. Technical Considerations（技術考量）

- **推薦引擎架構：** Personalized Route Recommendation 究竟是 rule-based、AI-based 或 hybrid，是原始輸入文件（第 14 節）中的開放問題——本文件不代為決定。
- **Route Fit 計算方式：** 同樣尚未定案。
- **相依性：** MVP 預期整合 Google Maps 或其他外部地圖／交通服務，以提供登山口與交通資訊——這在原始輸入文件中是明確標註的 `[assumption]`，並非已確認的技術決策。
- **資料來源：** 難度維度（坡度、地形、技術難度、風險）、交通／登山口資訊，以及 Route Timeline 資料應由哪個資料來源提供，尚未定案（第 14 節「Data/Technical」）。
- **風險：** 路線資料的可用性與品質，是一個牽動全局的未知數——幾乎所有 P0 功能（難度拆解、推薦、Route Fit、Timeline）都仰賴目前尚無確定來源的資料。

---

## 7. Implementation Plan（實作計畫）

- **Phase 1（MVP）：** 第 4 節列出的全部十一項 P0 功能需求——完整的 Find → Plan → Go 體驗。原始輸入文件並未進一步分級。
- **Phase 2／Phase 3：** 原始輸入文件未定義。依據 PRD 產出規範第 5 點與第 8 點，本文件不會捏造未來階段的內容。原始輸入文件第 12 節（Out of Scope）列出了明確排除於此次 MVP 之外、但自身狀態標註為「需要確認」的項目：即時 GPS 導航、緊急救援／SOS、登山社群網路、社群發文、裝備市集／電商、即時位置分享、進階訓練／體能追蹤。目前未定義這些項目未來重新納入範圍的條件。

---

## 8. Open Questions（未解決問題）

直接承接自原始輸入文件第 14 節，並依負責範疇整理，另加上本文件其他章節標示出的「狀態未完成」章節。原始素材中沒有任何一項指定負責人或期限——這件事本身也是一項待辦事項。

**Product（產品面）**
- 哪些 Hiking Profile 欄位為必填、哪些為選填？
- Hiking Profile 應該持續保存，還是每次行程都需要重新編輯？
- Route Fit 的定義是什麼？
- Route Fit 應該以分數、等級、文字說明，還是組合方式呈現？
- 為何 3–5 條推薦是最適區間？
- MVP 需要哪些 Route Difficulty 維度（除 US1 已列出的四項之外）？
- Suggested Time Schedule 應該個人化到什麼程度？
- Departure Checklist 應包含哪些項目？

**Research（研究面）**
- 依訪談證據來看，哪個 Journey 步驟的摩擦感最高？*（第 4 節目前尚無任何證據）*
- 哪些 P0 功能是依據已驗證的痛點，哪些主要建立在假設之上？
- 有哪些證據顯示使用者需要推薦理由的說明？
- 有哪些證據顯示規劃資訊分散是一個顯著的痛點？

**Data / Technical（資料／技術面）**
- 目前有哪些路線資料可用於難度拆解？
- 坡度、地形、技術難度與風險該如何計算或取得資料來源？
- 交通與登山口資訊的資料來源為何？
- 產生 Route Timeline 需要哪些資料？
- Personalized Route Recommendation 是 rule-based、AI-based 還是 hybrid？
- Route Fit 該如何計算？
- 當路線資料不完整或彼此衝突時該如何處理？

**Process / Governance（流程與治理，由本 PRD 提出，非原始輸入文件第 14 節內容）**
- 成功指標的基準值與目標值皆未設定——由誰負責埋點與量測，期限為何？
- Why Now／Strategic Alignment 皆未說明——在與其他專案比較優先順序前需要先補齊。
- 利害關係人（第 15 節）僅列出建議類別（PM、設計、前端、後端、若採 ML 推薦則需 Data/AI 工程師、登山安全領域專家、business stakeholder、如需要則加入法務／隱私審閱者）——尚未指派具體人選，也尚未確認審閱者名單。
- Out of Scope（第 12 節）標註為「需要確認」——尚未被正式核可為最終版本。

---

## 9. Appendix（附錄）

- 原始輸入文件：`personalized_hiking_prd_input.md`
- 範本與評分標準：`.agents/skills/prd-template/SKILL.md`
- 成功指標校準指南：`.agents/skills/prd-template/references/success-metrics-guide.md`
- 原始輸入文件未提供競品分析或其他研究連結。

---

## 自評分數（0–40 分制，依 skill 指示執行）

| 面向 | 分數 | 說明 |
|---|---|---|
| Problem grounding（問題扎根程度） | 5 / 10 | 問題陳述以使用者觀點撰寫且具體，但完全沒有引用研究或量化的現況數據——原始輸入文件第 4 節完全空白。 |
| Requirement testability（需求可驗證性） | 7 / 10 | P0 需求與驗收標準具體且可追溯，但部分 NFR 仍為樣板式主題、沒有具體門檻，部分驗收標準也仍繫於未解決的 Open Questions。 |
| Metric rigor（指標嚴謹度） | 3 / 10 | 指標*組合*合理（涵蓋 outcome、adoption、guardrail），但**沒有任何一項指標具備基準值或目標值**——這是本 PRD 最大的缺口。 |
| Scope & risk honesty（範圍與風險誠實度） | 8 / 10 | MVP 範圍明確限定在 P0 項目、Out of Scope 項目已記錄（雖未經確認），Open Questions 也相當完整——但都尚未指派負責人或期限。 |

**總分：23 / 40** ——低於 32 分以上的「可上線品質」門檻。要補齊差距，最重要的兩個槓桿是：（1）完成第 4 節的使用者研究，讓 Problem Statement 得以量化；（2）在下一版草稿前，為成功指標完成埋點並確立基準值。這兩點都已列入上方的 Open Questions。
