from playwright.sync_api import Page, expect
import pytest

# @pytest.mark.skip
# def test_static_web_table(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     table = page.locator("table[name='BookTable']")
#     expect(table).to_be_visible()

#     rows = table.locator("tr")
#     expect(rows).to_have_count(7)
#     row_count = rows.count()
#     print("row count: ", row_count)

#     cols = rows.locator("th")
#     expect(cols).to_have_count(4)
#     col_count = cols.count()
#     print("col count: ", col_count)


#     # Read all data form 2nd row
#     print("***************2nd Row data:*************** \n",rows.nth(2).locator("td").all_inner_texts())

#     #Read all rows data
#     print("***************All Rows data:*************** \n")
#     for row in rows.all()[1:]:
#         print(row.locator("td").all_inner_texts())

#     print("***************Author Mukesh's BookNames:***************")
#     for row in rows.all()[1:]:
#         author = row.locator("td").nth(1).inner_text()
#         if author == "Mukesh":
#             book_name = row.locator("td").nth(0).inner_text()
#             print(f"{author}\t:  {book_name}")

#     print("***************Total Price:***************")
#     total_price=0
#     for row in rows.all()[1:]:
#         price = row.locator("td").nth(3).inner_text()
#         total_price += int(price)
#     print("Total price is:", total_price)
