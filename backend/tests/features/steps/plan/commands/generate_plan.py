import parse
from behave import register_type, when


@parse.with_pattern(r"[^\"]*")
def parse_route_key(text):
    return text


register_type(RouteKey=parse_route_key)


@when('使用者 "{user_name}" 選定路線 "{route_key:RouteKey}" 生成登山規劃書')
def step_impl(context, user_name, route_key):
    headers = {}
    if user_name in context.ids:
        user_id = context.ids[user_name]
        token = context.jwt_helper.generate_token(str(user_id))
        headers["Authorization"] = f"Bearer {token}"

    request_body = {}
    if route_key:
        if route_key in context.ids:
            request_body["route_id"] = context.ids[route_key]
        else:
            # route_key 非已知的自然鍵（如 R99）：視為系統中不存在/不在推薦結果中的路線
            request_body["route_id"] = 999999

    response = context.api_client.post("/api/plans", json=request_body, headers=headers)
    context.last_response = response
