@command
Feature: 請求路線推薦

  Background:
    Given 系統已建立路線知識庫（含路線基礎資料、即時開放狀態、當日天氣預報），供 RAG 檢索使用
    And 候選知識庫資料來源包含：
      | 資料類型      | 候選來源                         |
      | 天氣預報      | 中央氣象署氣象資料開放平臺（鄉鎮/山區天氣預報） |
      | 步道即時開放狀態 | 林業及自然保育署台灣山林悠遊網開放資料       |
      | 步道/景點基礎資料 | 政府資料開放平臺                     |
    And 個人條件問卷包含以下題項：
      | 題號  | 題目               | 回答型態    | 是否必答 |
      | Q1  | 最近一年登山頻率         | 單選      | 必答   |
      | Q2  | 曾完成且最接近能力上限的路線與完成時體感 | 開放文字+單選 | 必答   |
      | Q3  | 一般天氣路況下可舒適完成的單日行程 | 單選      | 必答   |
      | Q4  | 已具備或能獨立操作的登山經驗類型 | 複選      | 必答   |
      | Q5  | 對各類登山情境的風險接受程度   | 矩陣單選    | 必答   |
      | Q6  | 偏好的行程節奏          | 單選      | 可略過  |
      | Q7  | 偏好的行程時間          | 單選      | 可略過  |
      | Q8  | 偏好的人潮狀況          | 單選      | 可略過  |
      | Q9  | 希望登山行程包含的體驗      | 複選      | 可略過  |
      | Q10 | 理想中的登山行程描述       | 開放文字    | 可略過  |
      | Q11 | 需特別考量的身體狀況或需求    | 複選      | 必答   |

  Rule: 前置（狀態）- 使用者必須已完成 Google 登入
    Example: 未登入時請求推薦操作失敗
      When 使用者 "Alice" 請求路線推薦
      Then 操作失敗，violation_type 為 "UNAUTHENTICATED"

  Rule: 前置（狀態）- 使用者必須已完成個人條件問卷的必答題項（Q1、Q2、Q3、Q4、Q5、Q11）
    Example: 問卷未完成時請求推薦操作失敗
      Given 系統中有以下使用者：
        | google_id | email           | name |
        | g-003     | bob@example.com | Bob  |
      And 使用者 "Bob" 已回答問卷：
        | question_code | answer_value  |
        | Q1             | 約每月1次      |
        | Q2             | 尚未完成過正式登山路線 |
        | Q3             | 3-4 小時       |
        | Q4             | 無             |
      When 使用者 "Bob" 請求路線推薦
      Then 操作失敗，violation_type 為 "PROFILE_INCOMPLETE"

  Rule: 前置（參數）- 推薦路線數量下限為 1 條、上限為 3 條
    Example: 符合路線超過 3 條時僅取前 3 條
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      And 系統中有以下路線：
        | route_id | name  | region | difficulty_level | open_status |
        | R1       | 路線一 | 北部   | easy              | open        |
        | R2       | 路線二 | 北部   | easy              | open        |
        | R3       | 路線三 | 中部   | moderate          | open        |
        | R4       | 路線四 | 中部   | moderate          | open        |
        | R5       | 路線五 | 南部   | moderate          | open        |
      When 使用者 "Alice" 請求路線推薦
      Then 操作成功
      And 推薦結果應包含 3 條路線

  Rule: 後置（回應）- 系統依使用者問卷條件（含風險承受度）以 RAG 架構（路線知識庫檢索 + LLM 排序）推薦符合條件的路線
    Example: 有符合條件路線時推薦 1~3 條
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      And 系統中有以下路線：
        | route_id | name  | region | difficulty_level | open_status |
        | R1       | 路線一 | 北部   | moderate          | open        |
        | R2       | 路線二 | 中部   | moderate          | open        |
      When 使用者 "Alice" 請求路線推薦
      Then 操作成功
      And 推薦結果應包含 2 條路線
      And 推薦結果應包含以下路線：
        | route_id | name  |
        | R1       | 路線一 |
        | R2       | 路線二 |

  Rule: 後置（回應）- 無符合條件路線時，顯示「無符合資料」
    Example: 無符合條件路線時顯示無符合資料
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      When 使用者 "Alice" 請求路線推薦
      Then 操作成功
      And 推薦結果應為「無符合資料」

  Rule: 後置（狀態）- 使用者可要求重新推薦
    Example: 使用者可連續請求推薦
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      And 系統中有以下路線：
        | route_id | name  | region | difficulty_level | open_status |
        | R1       | 路線一 | 北部   | moderate          | open        |
      When 使用者 "Alice" 請求路線推薦
      And 使用者 "Alice" 請求路線推薦
      Then 操作成功
