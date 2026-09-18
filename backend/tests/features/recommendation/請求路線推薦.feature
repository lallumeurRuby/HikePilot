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
      | 題號  | 題目               | 回答型態    | 是否必答 | 選項（代碼:文字） |
      | Q1  | 最近一年登山頻率         | 單選      | 必答   | Q1-1:幾乎沒有登山經驗, Q1-2:每半年約1-2次, Q1-3:每2-3個月約1次, Q1-4:約每月1-2次, Q1-5:約每週或每兩週1次, Q1-6:每週多次 |
      | Q2  | 曾完成且最接近能力上限的路線（路線名稱） | 開放文字    | 必答   | （無） |
      | Q2B | 上述路線完成時的體感       | 單選      | 必答   | Q2B-1:非常輕鬆, Q2B-2:輕鬆, Q2B-3:適中, Q2B-4:有挑戰但可完成, Q2B-5:非常吃力／接近極限, Q2B-6:中途放棄或需要協助 |
      | Q3  | 一般天氣路況下可舒適完成的單日行程 | 單選      | 必答   | Q3-1:2小時以內, Q3-2:2-4小時, Q3-3:4-6小時, Q3-4:6-8小時, Q3-5:8-10小時, Q3-6:10小時以上 |
      | Q4  | 已具備或能獨立操作的登山經驗類型 | 複選      | 必答   | Q4-1:一般步道健行, Q4-2:陡坡／連續階梯, Q4-3:原始山徑, Q4-4:碎石／岩石地形, Q4-5:拉繩／需手腳並用地形, Q4-6:夜間行走, Q4-7:地圖／離線地圖判讀, Q4-8:GPX導航, Q4-9:渡溪, Q4-10:高山過夜／山屋, Q4-11:露營／背負裝備, Q4-12:高海拔3000m以上, Q4-13:雪季／冰雪地形, Q4-14:無上述經驗 |
      | Q5  | 對各類登山情境的風險接受程度   | 矩陣單選    | 必答   | 情境（列）：steepness:陡峭上坡／下坡, scrambling:手腳並用攀爬, exposure:暴露感強的稜線／高落差地形, altitude:高海拔環境, navigation_difficulty:路徑不明顯／需要自行導航；接受程度（欄）：Q5-1:不接受, Q5-2:盡量避免, Q5-3:視情況可接受, Q5-4:可以接受, Q5-5:喜歡／主動選擇 |
      | Q6  | 偏好的行程節奏          | 單選      | 可略過  | Q6-1:悠閒，經常休息拍照, Q6-2:偏悠閒, Q6-3:適中, Q6-4:偏快，以完成路線為主, Q6-5:挑戰型，偏好高強度 |
      | Q7  | 偏好的行程時間          | 單選      | 可略過  | Q7-1:2小時以內, Q7-2:2-4小時, Q7-3:4-6小時, Q7-4:6-8小時, Q7-5:8-10小時, Q7-6:不限定 |
      | Q8  | 偏好的人潮狀況          | 單選      | 可略過  | Q8-1:熱門、人多也可以, Q8-2:有一些人比較安心, Q8-3:無特別偏好, Q8-4:偏好人少, Q8-5:越安靜、越少人越好 |
      | Q9  | 希望登山行程包含的體驗      | 複選      | 可略過  | Q9-1:山頂展望, Q9-2:日出, Q9-3:日落, Q9-4:森林, Q9-5:瀑布／溪流, Q9-6:湖泊, Q9-7:雲海, Q9-8:季節花卉／植物, Q9-9:野生動物／生態, Q9-10:歷史／人文遺跡, Q9-11:攝影, Q9-12:高山景觀, Q9-13:稜線行走, Q9-14:攀爬／刺激地形, Q9-15:溫泉, Q9-16:山屋／住宿體驗, Q9-17:露營, Q9-18:百岳／小百岳／山岳蒐集 |
      | Q10 | 理想中的登山行程描述       | 開放文字    | 可略過  | （無） |
      | Q11 | 需特別考量的身體狀況或需求    | 複選      | 必答   | Q11-1:無特殊需求, Q11-2:膝蓋容易不適, Q11-3:腳踝／足部容易不適, Q11-4:腰背容易不適, Q11-5:心肺耐力較弱, Q11-6:容易喘／需要較頻繁休息, Q11-7:懼高, Q11-8:容易暈眩, Q11-9:不適合長時間曝曬, Q11-10:不適合低溫環境, Q11-11:不適合高海拔, Q11-12:需要較頻繁補水／休息, Q11-13:其他 |

  Rule: 前置（狀態）- 使用者必須已完成 Google 登入
    Example: 未登入時請求推薦操作失敗
      When 使用者 "Alice" 請求路線推薦
      Then 操作失敗，violation_type 為 "UNAUTHENTICATED"

  Rule: 前置（狀態）- 使用者必須已完成個人條件問卷的必答題項（Q1、Q2、Q2B、Q3、Q4、Q5、Q11）
    Example: 問卷未完成時請求推薦操作失敗
      Given 系統中有以下使用者：
        | google_id | email           | name |
        | g-003     | bob@example.com | Bob  |
      And 使用者 "Bob" 已回答問卷：
        | question_code | answer_value  |
        | Q1             | Q1-4          |
        | Q2             | 尚未完成過正式登山路線 |
        | Q3             | Q3-2          |
        | Q4             | Q4-14         |
      When 使用者 "Bob" 請求路線推薦
      Then 操作失敗，violation_type 為 "PROFILE_INCOMPLETE"

  Rule: 前置（參數）- 推薦路線數量下限為 1 條、上限為 3 條
    Example: 符合路線超過 3 條時僅取前 3 條
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value                                |
        | Q1             | Q1-6                                        |
        | Q2             | 郊山一日健行                                 |
        | Q2B            | Q2B-2                                       |
        | Q3             | Q3-4                                        |
        | Q4             | Q4-7,Q4-9                                    |
        | Q5             | steepness:Q5-4,scrambling:Q5-1,exposure:Q5-2,altitude:Q5-3,navigation_difficulty:Q5-3 |
        | Q11            | Q11-1                                       |
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
        | question_code | answer_value                                |
        | Q1             | Q1-6                                        |
        | Q2             | 郊山一日健行                                 |
        | Q2B            | Q2B-2                                       |
        | Q3             | Q3-4                                        |
        | Q4             | Q4-7,Q4-9                                    |
        | Q5             | steepness:Q5-4,scrambling:Q5-1,exposure:Q5-2,altitude:Q5-3,navigation_difficulty:Q5-3 |
        | Q11            | Q11-1                                       |
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
        | question_code | answer_value                                |
        | Q1             | Q1-6                                        |
        | Q2             | 郊山一日健行                                 |
        | Q2B            | Q2B-2                                       |
        | Q3             | Q3-4                                        |
        | Q4             | Q4-7,Q4-9                                    |
        | Q5             | steepness:Q5-4,scrambling:Q5-1,exposure:Q5-2,altitude:Q5-3,navigation_difficulty:Q5-3 |
        | Q11            | Q11-1                                       |
      When 使用者 "Alice" 請求路線推薦
      Then 操作成功
      And 推薦結果應為「無符合資料」

  Rule: 後置（狀態）- 使用者可要求重新推薦
    Example: 使用者可連續請求推薦
      Given 系統中有以下使用者：
        | google_id | email              | name  |
        | g-001     | alice@example.com  | Alice |
      And 使用者 "Alice" 已回答問卷：
        | question_code | answer_value                                |
        | Q1             | Q1-6                                        |
        | Q2             | 郊山一日健行                                 |
        | Q2B            | Q2B-2                                       |
        | Q3             | Q3-4                                        |
        | Q4             | Q4-7,Q4-9                                    |
        | Q5             | steepness:Q5-4,scrambling:Q5-1,exposure:Q5-2,altitude:Q5-3,navigation_difficulty:Q5-3 |
        | Q11            | Q11-1                                       |
      And 系統中有以下路線：
        | route_id | name  | region | difficulty_level | open_status |
        | R1       | 路線一 | 北部   | moderate          | open        |
      When 使用者 "Alice" 請求路線推薦
      And 使用者 "Alice" 請求路線推薦
      Then 操作成功
