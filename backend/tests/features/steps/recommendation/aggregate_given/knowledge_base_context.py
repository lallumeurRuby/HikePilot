from behave import given

# Background 描述性語句：說明知識庫的存在與資料來源，不對應具體 Aggregate 寫入。
# 實際的路線資料由「系統中有以下路線：」步驟（routes.py）建立。


@given(
    "系統已建立路線知識庫（含路線基礎資料、即時開放狀態、當日天氣預報），供 RAG 檢索使用"
)
def step_impl(context):
    pass


@given("候選知識庫資料來源包含：")
def step_impl(context):
    pass
