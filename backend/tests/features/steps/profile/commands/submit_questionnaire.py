from behave import when


@when('使用者 "{user_name}" 提交問卷回答：')
def step_impl(context, user_name):
    answers = [
        {"question_code": row["question_code"], "answer_value": row["answer_value"]}
        for row in context.table
    ]
    request_body = {"answers": answers}

    headers = {}
    if user_name in context.ids:
        user_id = context.ids[user_name]
        token = context.jwt_helper.generate_token(str(user_id))
        headers["Authorization"] = f"Bearer {token}"

    response = context.api_client.post(
        "/api/profile/questionnaire", json=request_body, headers=headers
    )
    context.last_response = response
