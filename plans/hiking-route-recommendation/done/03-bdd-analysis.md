# Phase 03: BDD Analysis（外部品質 — 可執行規格）

## 審查進度

- [x] 03.1 相關規格已審查 — **簽名**: 2026-09-18 10:24
- [x] 03.2 交付物已審查 — **簽名**: 2026-09-18 12:21（重新審核 Change Log 後再次簽核）

> **重新開放原因**：Phase 05 Backend TDD 執行時，Red 階段發現 2 個 Feature Files 有缺口（見下方
> change log），已直接修正 SSOT（`specs/features/`）。因交付物內容已變更，需重新審核後才能維持
> Phase 03 簽核狀態。
>
> **Change Log**（2026-09-18，由 Phase 05 TDD 回饋觸發）：
> 1. `profile/填寫個人條件問卷.feature` — Rule「後置（狀態）- 可選擇是否更新問卷答案」的 Example
>    「再次提交覆蓋既有答案」，原本的 Given「已回答問卷」只給了 Q1 一題，但必答題共 6 題
>    （Q1/Q2/Q3/Q4/Q5/Q11）。這個初始狀態本身無法通過必填驗證，測不出「覆蓋更新」這個真正要驗證的
>    行為。已補齊 Q2/Q3/Q4/Q5/Q11，使 Given 狀態與 Example 1（必答齊全）一致。
> 2. `recommendation/請求路線推薦.feature` — Background 原本只有路線知識庫的 Given，缺少「個人條件
>    問卷包含以下題項：」的題目目錄。共用的「已回答問卷」Given step 需要這份題目目錄才能解析/驗證
>    answer_value（判斷必答/選填、型態），這是 profile domain 已有、但 recommendation domain 引用
>    同一 Given 句型時遺漏的前置資料。已補上與 profile 一致的題目目錄表。

## 目的 (What)

從已確認的 Feature Rules（Phase 01）+ 實體結構（Phase 02）推導最小必要句型集，
填入具體 Examples，將 Feature Files 從「行為骨架」升級為「可執行規格」。

**三階段推導**：系統抽象 → 句型模型 → Feature with Examples。
每個階段都需使用者審核才能進入下一個。

**Reconciler 模式**：bdd-analysis 以三層 desired-state reconciliation 運作——每層各自 derive desired → read current → compute diff → preview → apply。讀取 Execution Plan 中 Phase 03 的 scope 決定哪些 domain 需分析。

**Boundary 偵測**：若偵測到 erm.dbml（Phase 02 已完成），
載入 web-backend preset（句型分析方針 + Handler 決策樹）。

觸發 skill：`/aibdd-form-bdd-analysis`

**依賴**：Phase 02 必須在 `done/` 中。

## 相關規格

| # | 規格 | 來源 | 說明 |
|---|------|------|------|
| 1 | Execution Plan | Phase 01 交付 | 本 Phase 的工作範圍（哪些 domain 需分析） |
| 2 | Feature Files（Rules） | Phase 01 交付 | CiC 歸零的行為骨架 |
| 3 | erm.dbml | Phase 02 交付 | 實體結構——欄位、型別、約束 |

## 交付物

carry-on Step 03.2 觸發時：

1. **DELEGATE `/aibdd-form-bdd-analysis`**，傳入：
   - features 資料夾路徑（`specs/features/`）
   - 澄清紀錄路徑（`specs/clarify/`）
   - Execution Plan scope（Phase 03 區段）
2. bdd-analysis 以 Reconciler 模式依序執行三階段（每層各自 reconcile）：
   - **系統抽象推導** → 展示並等待使用者審核
   - **各 domain 句型模型推導** → 展示並等待使用者審核
   - **產出 Feature Files（填入 Examples）** → 展示摘要並等待使用者審核
3. 完成後回傳控制權

| # | 交付物 | 路徑 | 狀態 |
|---|--------|------|------|
| 03.1 | 系統抽象 | `specs/features/系統抽象.md` | DONE |
| 03.2 | 句型模型 | `specs/features/{domain}/句型.md` | DONE |
| 03.3 | Feature Files（含 Examples） | `specs/features/**/*.feature` | DONE |

### 驗收點

- [x] `features/系統抽象.md` 產出並經使用者審核
- [x] 每個 domain 的 `features/{domain}/句型.md` 產出並經使用者審核
- [x] 所有 .feature 填入具體 Examples
- [x] 所有 .feature 移除 `@ignore` tag
- [x] QA 五維分析完整（每行 Example 有存在理由）
