import json

from behave import when


@when("使用者以 Google 帳號登入：")
def step_impl(context):
    row = context.table[0]
    fake_id_token = json.dumps(
        {"google_id": row["google_id"], "email": row["email"], "name": row["name"]}
    )

    response = context.api_client.post("/api/auth/google", json={"id_token": fake_id_token})
    context.last_response = response
