from playwright.sync_api import Page, expect
import time
import pytest


# @pytest.mark.skip
# def test_playwright_basics(playwright):# This test we can run even without importing anything as here playwright is a fixture. 
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.google.com")

# @pytest.mark.skip
# def  test_playwright_shotcut_pagefixture(page: Page):
#     page.goto("https://www.facebook.com")
#     page.get_by_label("Email or mobile number").fill("abc@gmail.com")
#     time.sleep(5)
#     page.get_by_label("Password").fill("password123")
#     page.get_by_role("button", name="Log In").click()
#     expect(page.get_by_text("The login information you entered is incorrect. ")).to_be_visible()  
#     time.sleep(10)

# @pytest.mark.skip
# def  test_playwright_firefox(playwright):
#     browser = playwright.firefox.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.facebook.com")
#     page.get_by_label("Email or mobile number").fill("abc@gmail.com")
#     time.sleep(5)
#     page.get_by_label("Password").fill("password123")
#     page.get_by_role("button", name="Log In").click()
#     expect(page.get_by_text("The login information you entered is incorrect. ")).to_be_visible()  
#     time.sleep(10)    

# @pytest.mark.skip
# def test_core_locators(page:Page):
#     page.goto("https://rahulshettyacademy.com/loginpagePractise/")
#     page.get_by_label("Username:").fill("rahulshettyacademy ")
#     page.get_by_label("Password:").fill("Learning@830$3mK2")
#     page.get_by_role("combobox").select_option("teach")
#     page.locator("#terms").check()    # page.get_by_label("I Agree to the ").click()
#     page.get_by_role("link", name="Forgot password?").click()
#     page.get_by_role("button", name="Sing In").click()
#      time.sleep(5)

"""
CSS Selector: 
id:"terms"          -> #terms
class="text-info    -> .text-info 
"""

