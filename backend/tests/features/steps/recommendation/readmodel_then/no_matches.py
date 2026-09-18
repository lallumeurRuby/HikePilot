from behave import then


@then("推薦結果應為「無符合資料」")
def step_impl(context):
    data = context.last_response.json()["data"]
    assert (
        data["has_matches"] is False
    ), f"預期 has_matches=false（無符合資料），實際 {data['has_matches']}"
    assert data["routes"] == [], f"預期無路線，實際 {data['routes']}"
