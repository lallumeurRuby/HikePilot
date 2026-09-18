# Execution Plan

需求：根據新手使用者的個人條件與風險承受度、路線即時資訊與當日天氣，推薦 1~3 條安全登山路線；
使用者選定路線後，生成含 8 大區塊的登山規劃書。

起始狀態：Greenfield（`specs/` 下無既有 activities / features / entity / api）。

明確排除本次範圍（使用者於 Flow Alignment 階段決定另立需求群組）：地圖疊圖顯示、GPS 追蹤定位、
Apple Health 整合、登山後數據回饋推薦機制。

## 概覽

| 類型 | 數量 |
|------|------|
| Create | 4 個 Feature（1 個 Activity、1 個 Actor） |
| Modify | 0 |
| Delete | 0 |

## Phase 02: Entity Modeling

| 操作 | 目標 | 說明 |
|------|------|------|
| create | User | Google OAuth 帳號（google_id、email 等） |
| create | UserProfile / QuestionnaireAnswer | 個人條件問卷回答（Q1-Q11，含必答/選填區分） |
| create | Route / RouteKnowledgeBase | 路線基礎資料，供 RAG 檢索使用（知識庫語料） |
| create | Recommendation | 一次推薦請求的結果紀錄（1~3 條路線） |
| create | HikingPlan | 登山規劃書（8 大區塊內容、PDF 產出） |

候選外部資料來源（供欄位設計參考）：中央氣象署氣象資料開放平臺（天氣預報）、
林業及自然保育署台灣山林悠遊網開放資料（步道開放狀態）、政府資料開放平臺（步道基礎資料）。

## Phase 03: BDD Analysis

| 操作 | 目標 | 說明 |
|------|------|------|
| create | auth/ domain | 全新 domain，Google 登入/註冊句型與 Examples |
| create | profile/ domain | 全新 domain，問卷填寫/更新句型與 Examples |
| create | recommendation/ domain | 全新 domain，RAG 推薦句型與 Examples |
| create | plan/ domain | 全新 domain，規劃書生成句型與 Examples |

## Phase 04: API Contract

| 操作 | 目標 | 說明 |
|------|------|------|
| create | POST /auth/google | Google OAuth 登入/註冊（單一 endpoint，upsert 語意） |
| create | POST /profile/questionnaire | 建立/更新個人條件問卷回答 |
| create | POST /recommendations | 請求路線推薦（RAG） |
| create | POST /plans | 選定路線並生成登山規劃書（PDF） |

Tech-Preference（使用者指定，供本 Phase 設計參考）：推薦機制採 RAG 架構
（路線資料建立可檢索知識庫，LLM 依使用者條件檢索+排序，而非 LLM 自行搜尋）；
Google OAuth 使用獨立的 Client 專案。

## Phase 05-07: Implementation

| 操作 | 目標 | 說明 |
|------|------|------|
| red-green-refactor | auth/使用者透過Google登入.feature | 新 feature 的 TDD |
| red-green-refactor | profile/填寫個人條件問卷.feature | 新 feature 的 TDD |
| red-green-refactor | recommendation/請求路線推薦.feature | 新 feature 的 TDD，含 RAG 檢索邏輯 |
| red-green-refactor | plan/生成登山規劃書.feature | 新 feature 的 TDD，含 PDF 產出 |
| frontend | 問卷填寫頁、推薦結果頁（含重新推薦）、規劃書下載頁 | Next.js Walking Skeleton 上建置 |

## IMPL_IMPACT（由 Phase 02-04 Reconciler 回填）

| Phase | 影響目標 | Impact Type | 來源 | 說明 |
|-------|---------|-------------|------|------|
| 05 | — | NEW_OPERATION | Phase 01 | Greenfield，四個 Feature 皆為全新操作 |
| 06 | — | NEW_OPERATION | Phase 01 | Greenfield，四個頁面皆為全新操作 |
| 07 | test-plans/ | — | Phase 01 | Activity 結構建立後需產出對應 Test Plan |
