@command
Feature: 使用者透過 Google 登入/註冊

  Rule: 前置（狀態）- 使用者必須持有可用的 Google 帳號
    # Google OAuth 流程本身把關使用者是否持有可用帳號，不在本系統可測試邊界內，不產生 Example

  Rule: 後置（狀態）- 使用者首次以 Google 帳號登入時，系統建立對應的 HikePilot 帳號
    Example: 新使用者首次登入時建立帳號並導向問卷
      When 使用者以 Google 帳號登入：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      Then 操作成功
      And 回應應包含 is_new_user 為 true，next_step 為 "questionnaire"

  Rule: 後置（狀態）- 使用者非首次登入時，系統以既有帳號完成登入
    Example: 既有使用者登入時不重複建立帳號
      Given 系統中有以下使用者：
        | google_id | email            | name |
        | g-002     | bob@example.com  | Bob  |
      When 使用者以 Google 帳號登入：
        | google_id | email            | name |
        | g-002     | bob@example.com  | Bob  |
      Then 操作成功
      And 回應應包含 is_new_user 為 false

  Rule: 後置（狀態）- 首次登入的使用者導向個人條件問卷填寫
    # 同一 Example 已涵蓋此規則 — 見上方「後置（狀態）- 使用者首次以 Google 帳號登入時」之 Example
