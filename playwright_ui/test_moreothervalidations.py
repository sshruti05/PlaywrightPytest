from playwright.sync_api import Page, expect
import pytest 
""" module contains below tests examples:
    -placeholder
    -alert
    -iframe
"""
# @pytest.mark.skip
# def test_placeholder(page: Page):
#     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
#     expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
#     page.get_by_role("button", name="Hide").click()
#     expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

# @pytest.mark.skip
# def test_alertboxcheck(page:Page):
#     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
#     page.on("dialog", lambda dialog: dialog.accept())
#     page.get_by_role("button", name="Confirm").click()


# @pytest.mark.skip
# def test_iframe_check(page:Page):
#     page.goto("https://jqueryui.com/autocomplete/")
#     locator = page.frame_locator("iframe.demo-frame")
#     locator.get_by_label("Tags: ").fill("Hello")
#     page.wait_for_timeout(3000)
#     page.get_by_placeholder("Search").fill("Draggable")
#     page.get_by_text("Draggable Widget › Options").click()
#     page.locator("#content").get_by_text("Draggable Widget")



    
    #Print col 2 whole rows
    # for row in rows.all()[1:]:
    #     if cols.nth(index).
    # index for index in range(cols+1) if cols.nth(index).locator("td",text).
    # selected_col = cols.filter(has_text="Subject")
    # col_index = selected_col.
    # col_count = rows.locator("td").count()

    # for count in range(1,col_count+1):



# def test_webtable(page:Page):
#     page.goto("https://practice.expandtesting.com/dynamic-table")
#     table = page.locator(".table table-striped")
#     col = table.get_by_text("Network")