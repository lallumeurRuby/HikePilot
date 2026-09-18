@command
Feature: 填寫/更新個人條件問卷

  Background:
    Given 個人條件問卷包含以下題項：
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
    Example: 未登入時提交問卷操作失敗
      When 使用者 "Alice" 提交問卷回答：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      Then 操作失敗，violation_type 為 "UNAUTHENTICATED"

  Rule: 前置（參數）- Q1、Q2、Q3、Q4、Q5、Q11 為必答題，Q6-Q10 可選擇不回答
    Example: 必答題全部填寫、選填題略過時操作成功
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      When 使用者 "Alice" 提交問卷回答：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      Then 操作成功

  Rule: 前置（參數）- 必答題未填寫時，操作失敗
    Example: 必答題缺漏時操作失敗
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      When 使用者 "Alice" 提交問卷回答：
        | question_code | answer_value          |
        | Q1             | 幾乎每週都有登山         |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q11            | 無特殊身體狀況           |
      Then 操作失敗，violation_type 為 "MISSING_REQUIRED_ANSWER"

  Rule: 後置（狀態）- 使用者於每次請求路線推薦前，可選擇是否更新問卷答案
    Example: 再次提交覆蓋既有答案
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value          |
        | Q1             | 約每月1次              |
        | Q2             | 已完成郊山一日健行，體感輕鬆 |
        | Q3             | 6-8 小時               |
        | Q4             | 地圖判讀, 溪谷渡溪        |
        | Q5             | 陡峭石階:可接受, 需垂降地形:不接受 |
        | Q11            | 無特殊身體狀況           |
      When 使用者 "Alice" 提交問卷回答：
        | question_code | answer_value    |
        | Q1             | 幾乎每週都有登山 |
      Then 操作成功
      And 使用者 "Alice" 的問卷回答 "Q1" 應為 "幾乎每週都有登山"
