from playwright.sync_api import Page, Route, expect

def intercept_request(route:Route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69de7245f86ba00005653e2e")

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)

    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button").filter(has_text="ORDERS").click()
    page.get_by_role("button").filter(has_text="View").first.click()
    message = page.locator(".blink_me").text_content()
    assert message == "You are not authorize to view this order"
