from behave import then


@then("推薦結果應包含 {count:d} 條路線")
def step_impl(context, count):
    data = context.last_response.json()["data"]
    actual_count = len(data["routes"])
    assert actual_count == count, f"預期 {count} 條路線，實際 {actual_count} 條"
