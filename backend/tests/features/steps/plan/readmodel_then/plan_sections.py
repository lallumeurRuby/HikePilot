from behave import then


@then("規劃書應包含以下區塊：")
def step_impl(context):
    data = context.last_response.json()["data"]
    actual_sections = data["sections"]

    expected = [
        {
            "section_order": int(row["section_order"]),
            "section_name": row["section_name"],
        }
        for row in context.table
    ]
    actual = [
        {"section_order": s["section_order"], "section_name": s["section_name"]}
        for s in actual_sections
    ]

    assert actual == expected, f"預期區塊 {expected}，實際 {actual}"
