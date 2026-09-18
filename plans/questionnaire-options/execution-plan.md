# Execution Plan — questionnaire-options

## 決策摘要（Clarify Loop 已確認）

- **Q5 矩陣列（情境）**：`steepness`（陡峭上坡／下坡）、`scrambling`（手腳並用攀爬）、`exposure`（暴露感強的稜線／高落差地形）、`altitude`（高海拔環境）、`navigation_difficulty`（路徑不明顯／需要自行導航）。矩陣欄（接受程度）沿用使用者提供的 5 段量表。
- **Q2 拆分**：新增題號 `Q2B`（體感，single_choice，必答），原 `Q2` 改為純「路線名稱」（open_text，必答）。不使用單一字串編碼複合答案。

## 選項代碼方案

代碼格式：`{題號}-{序}`（例如 `Q1-1`）。Multi-choice 答案以逗號分隔多個代碼儲存於既有 `answer_value` 欄位（沿用現有慣例，如 Q4 原範例 `"地圖判讀, 溪谷渡溪"` → 改為 code）。Matrix（Q5）以 `情境代碼:等級代碼` 逗號分隔儲存，例如 `steepness:Q5-4,scrambling:Q5-1`。

## 概覽

| 類型 | 數量 |
|------|------|
| Modify | 11（Q1,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q11 補選項；Q2 改題目範圍；Q10 不變但需確認無選項） |
| Create | 1（新題號 Q2B） |
| Delete | 0 |

## Phase 02: Entity Modeling

| 操作 | 目標 | 說明 |
|------|------|------|
| create | `questionnaire_question_option` 表 | 欄位：id, question_code(FK), option_code(unique per question), option_text, display_order |
| create | `questionnaire_question_scenario` 表（Q5 專用） | 欄位：id, question_code(FK, ='Q5'), scenario_code, scenario_text, display_order（若判斷可與 option 表合併則於 Phase 02 決定） |
| modify | `questionnaire_question` seed 資料 | Q2 題目文字收斂為「路線名稱」；新增 Q2B 列（code, question_text='曾完成且最接近能力上限的路線——完成時體感', answer_type=single_choice, is_required=true, display_order 緊接 Q2 之後，其後題號 display_order 順延） |

## Phase 03: BDD Analysis

| 操作 | 目標 | 說明 |
|------|------|------|
| modify | `specs/features/profile/填寫個人條件問卷.feature` Background | 表格新增「選項」欄；Q2 列改為僅路線名稱；新增 Q2B 列；Q5 補充情境清單說明 |
| modify | 既有 4 個 Example（Rule 內） | 原本以自然語言字串填答（如「幾乎每週都有登山」），改為對應選項代碼（如 `Q1-6`）；Q4/Q9/Q11 改為逗號分隔代碼；Q5 改為 `情境代碼:等級代碼` 格式；新增 Q2B 答案列 |

## Phase 04: API Contract

| 操作 | 目標 | 說明 |
|------|------|------|
| modify | `specs/api/api.yml` `SubmitQuestionnaireRequest` | `question_code` enum 加入 `Q2B`；`answer_value` 說明改為選項代碼編碼規則 |
| modify | `specs/api/api.yml` `ErrorResponse.violation_type` | 新增 `INVALID_OPTION_CODE` |

**發現**：目前系統沒有「取得問卷題項」的 GET endpoint——前端 `mockQuestionnaireQuestions` 與後端 seed 資料是各自獨立維護的靜態清單（既有架構慣例，非本次變更引入）。因此選項清單（`options`/`scenarios`）**不經過 API 傳輸**，而是分別寫入前端 fixtures 與後端 seed/migration，兩邊各自持有一份。此為既有慣例的延伸，不新增 GET endpoint（避免超出 Execution Plan 範圍）。

## Phase 05-07: Implementation

| 操作 | 目標 | 說明 |
|------|------|------|
| red-green-refactor | `backend/app/models/questionnaire_question.py` + 新 option/scenario model | 新增關聯與 migration |
| red-green-refactor | `backend/app/repositories/questionnaire_question_repository.py` | 讀取時 join 選項 |
| red-green-refactor | `backend/app/services/questionnaire_service.py` | 回傳含選項的題項；驗證 answer_value 是否為合法代碼（如需要） |
| frontend-build | `frontend/src/lib/types/questionnaire.schema.ts` | `QuestionCodeSchema` 加入 `Q2B`；`QuestionnaireQuestion` 型別加 `options` / `scenarios` |
| frontend-build | `frontend/src/mocks/fixtures.ts` | 補上每題 `options`／Q5 `scenarios`，更新 `mockAliceAnswers` 為新代碼格式 |
| frontend-build | `frontend/src/app/(protected)/questionnaire/page.tsx` | 依 `answer_type` 分流渲染：single_choice→radio、multi_choice→checkbox、matrix_single_choice→矩陣、open_text→維持文字框 |

## IMPL_IMPACT（Phase 02-04 完成後回填）

| Phase | 影響目標 | Impact Type | 來源 | 說明 |
|-------|---------|-------------|------|------|
| 05 | models/questionnaire_question_option | NEW_TABLE | Phase 02 | 新增選項表 |
| 05 | migrations/ | FIELD_CHANGE | Phase 02 | 新表 + Q2B 種子資料 + Q2 題目文字調整 |
| 05 | step_defs/profile | DATATABLE_SCHEMA | Phase 03 | Background/Example 新代碼格式 |
| 06 | mocks/fixtures.ts | ENDPOINT_SCHEMA | Phase 04 | +options / +scenarios |
| 06 | pages/questionnaire/page.tsx | ENDPOINT_SCHEMA | Phase 04 | UI 依 answer_type 分流 |
| 07 | test-plans/ | — | Phase 01 | Q2 拆分為 Q2B，行為結構變更需重新確認測試腳本涵蓋兩題 |
