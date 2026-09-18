@command
Feature: 生成登山規劃書

  Background:
    Given 使用者已取得路線推薦結果

  Rule: 前置（狀態）- 使用者必須從推薦結果中選定一條路線
    Example: 未指定路線時操作失敗
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已取得以下路線推薦結果：
        | route_id | name  |
        | R1       | 路線一 |
        | R2       | 路線二 |
      When 使用者 "Alice" 選定路線 "" 生成登山規劃書
      Then 操作失敗，violation_type 為 "ROUTE_NOT_SELECTED"

    Example: 選定非推薦結果中的路線時操作失敗
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已取得以下路線推薦結果：
        | route_id | name  |
        | R1       | 路線一 |
        | R2       | 路線二 |
      When 使用者 "Alice" 選定路線 "R99" 生成登山規劃書
      Then 操作失敗，violation_type 為 "ROUTE_NOT_IN_RECOMMENDATION"

  Rule: 後置（回應）- 系統依「個人條件 + 推薦結果 + 公開資料」生成登山規劃書
    Example: 選定推薦結果中的路線成功生成規劃書
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已取得以下路線推薦結果：
        | route_id | name  |
        | R1       | 路線一 |
        | R2       | 路線二 |
      When 使用者 "Alice" 選定路線 "R1" 生成登山規劃書
      Then 操作成功
      And 規劃書應包含以下區塊：
        | section_order | section_name              |
        | 1              | 路線摘要                   |
        | 2              | 分段行程                   |
        | 3              | 天氣路況                   |
        | 4              | 風險應對                   |
        | 5              | 裝備補給                   |
        | 6              | 交通資訊                   |
        | 7              | 緊急應變（撤退條件、替代方案） |
        | 8              | 行前 Checklist             |
      And 規劃書應提供可下載的 PDF 連結

  Rule: 後置（回應）- 規劃書須包含以下區塊：
    | 區塊順序 | 區塊名稱          |
    | 1    | 路線摘要          |
    | 2    | 分段行程          |
    | 3    | 天氣路況          |
    | 4    | 風險應對          |
    | 5    | 裝備補給          |
    | 6    | 交通資訊          |
    | 7    | 緊急應變（撤退條件、替代方案） |
    | 8    | 行前 Checklist    |
    # 同一 Example 已涵蓋此規則 — 見上方「後置（回應）- 系統依「個人條件 + 推薦結果 + 公開資料」生成登山規劃書」之 Example

  Rule: 後置（回應）- 規劃書以可下載的 PDF 形式呈現
    # 同一 Example 已涵蓋此規則 — 見上方「後置（回應）- 系統依「個人條件 + 推薦結果 + 公開資料」生成登山規劃書」之 Example
