from playwright.sync_api import Page,  expect
import time

# def test_mouse_hover(page:Page):
#     page.goto("https://practice.expandtesting.com/hovers")
#     page.get_by_test_id("img-user-1").hover()
#     page.get_by_role("link", name="View profile").click()
#     expect(page.locator("h2")).to_contain_text("Welcome user1")
#     time.sleep(50)  