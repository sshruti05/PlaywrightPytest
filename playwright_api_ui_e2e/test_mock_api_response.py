from playwright.sync_api import Page, Route

fake_order_res_payload = {"data":[], "message": "No Ordersssssss"}
def intercept_response(route:Route):
    print("Entered in Route code")
    route.fulfill(
        json = fake_order_res_payload
    )
    print("Out of route code")

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")

    page.route("**/api/ecom/order/get-orders-for-customer/*",intercept_response)

    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.locator("button").filter(has_text="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)