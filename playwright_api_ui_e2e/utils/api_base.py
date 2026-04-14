from playwright.sync_api import Playwright

login_req_payload = '{"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}'
create_order_payload='{"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}'

class APIUtils:
    def get_token(self, playwright:Playwright):
        req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = req_context.post("/api/ecom/auth/login",
            data = login_req_payload,
            headers = {"Content-Type":"application/json"})  
        assert response.status == 200 #assert response.ok
        response_body = response.json()
        return response_body["token"]

    def createOrderApiCall(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = create_order_payload,
                                 headers={"Authorization":self.get_token(playwright), 
                                          "Content-Type":"application/json"})
        print(response.json())
        return response.json()["orders"][0]