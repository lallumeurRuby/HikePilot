from behave import then


@then("規劃書應提供可下載的 PDF 連結")
def step_impl(context):
    data = context.last_response.json()["data"]
    pdf_url = data.get("pdf_url")
    assert pdf_url, f"預期提供 pdf_url，實際 {pdf_url!r}"
