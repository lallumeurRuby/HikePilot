from behave import when


@when('使用者 "{user_name}" 請求路線推薦')
def step_impl(context, user_name):
    headers = {}
    if user_name in context.ids:
        user_id = context.ids[user_name]
        token = context.jwt_helper.generate_token(str(user_id))
        headers["Authorization"] = f"Bearer {token}"

    response = context.api_client.post("/api/recommendations", headers=headers)
    context.last_response = response
