from playwright.sync_api import Page, expect

# def test_dynamic_web_table(page:Page):
#     page.goto("https://testautomationpractice.blogspot.com/")
#     table = page.locator("table#taskTable")
#     expect(table).to_be_visible()

#     columns = table.locator("th")
#     col_count = columns.count()
#     print("Col count is:",col_count)

#     rows Row= table.locator("tbody tr")
#     row_count = rows.count()
#     print("Row count is:",row_count)

#     #identify target column
#     col_index = 0
#     for index in range(col_count):
#         print("Col value is:", index)
#         if columns.nth(index).filter(has_text="Disk (MB/s)").count()>0:
#             col_index = index
#             break
#     print("Disk index is: ", col_index)
    
#     #identify target row 
#     for row in rows.all()[1:]:
#         if row.locator("td").filter(has_text = "Firefox").count()>0:
#             result_value = row.locator("td").nth(col_index).inner_text()
#             print(":firefox and Col:Dish has value as", result_value)