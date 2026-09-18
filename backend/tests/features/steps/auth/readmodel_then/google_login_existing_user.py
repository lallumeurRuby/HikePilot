from behave import then


@then("回應應包含 is_new_user 為 {is_new_user_str:w}")
def step_impl(context, is_new_user_str):
    data = context.last_response.json()["data"]
    expected_is_new_user = is_new_user_str.strip().lower() == "true"

    assert (
        data["is_new_user"] == expected_is_new_user
    ), f"預期 is_new_user={expected_is_new_user}，實際 {data['is_new_user']}"
