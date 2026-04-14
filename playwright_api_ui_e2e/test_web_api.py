from playwright.sync_api import Playwright, expect

from utils.api_base import APIUtils

def test_e2e_web_api(playwright:Playwright): 
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> OrderId
    api_util_obj = APIUtils()
    order_id = api_util_obj.createOrderApiCall(playwright)
    

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    page.locator("button").filter(has_text="ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
