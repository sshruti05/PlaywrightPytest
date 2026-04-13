from playwright.sync_api import Page, expect
import pytest
import time

@pytest.mark.skip
def test_uivalidation_dynamic_script(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()    # page.get_by_label("I Agree to the ").click()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button").click()
    blackberry_product = page.locator("app-card").filter(has_text="Blackberry")
    blackberry_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

# Navigation to new window
@pytest.mark.skip
def test_childwindowhandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_page() as new_page_info:
        page.get_by_role("link").get_by_text("Free Access").click()
        child_page = new_page_info.value
        expect(child_page).to_have_title("RS Academy")
        text = child_page.locator(".red").text_content()
        print(text)
        word = text.split("at")
        email = word[1].strip().split(" ")[0]
        print("*********************    ",email)
        assert email == "mentor@rahulshettyacademy.com"
        time.sleep(5)




    