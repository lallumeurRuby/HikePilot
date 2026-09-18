from behave import then


@then("推薦結果應包含以下路線：")
def step_impl(context):
    data = context.last_response.json()["data"]
    actual_routes = data["routes"]

    expected = [
        {"route_id": context.ids[row["route_id"]], "name": row["name"]}
        for row in context.table
    ]
    actual = [{"route_id": r["route_id"], "name": r["name"]} for r in actual_routes]

    for expected_route in expected:
        assert (
            expected_route in actual
        ), f"預期路線 {expected_route} 出現在推薦結果 {actual} 中"
