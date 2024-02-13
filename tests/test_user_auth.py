import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


'''' '''

@allure.epic("Auth case")
class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup_method(self):
        ''' data = {
            'email': 'zhenya_shalanova@mail.ru',
            'password': '12345'
        }  '''
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post("/user/login", data=data)
        #response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        #assert "auth_sid" in response.cookies, "There is no auth cookie"
        #assert "x-csrf-token" in response.headers, "There is no csrf header"


        self.auth_sid = self.get_cookie(response, "auth_sid")
        self.token = self.get_header(response, "x-csrf-token")
        self.user_id = self.get_json_value(response, "user_id")

        #assert "user_id" in response.json(), "There is no user_id"
        #self.auth_sid = response.cookies.get("auth_sid")
        #self.token = response.headers.get("x-csrf-token")
        #self.user_id = response.json()["user_id"]

    @allure.description("Success test auth")
    @allure.severity("value = SeverityLevel.BLOCKER")
    @allure.step("Start test")
    def test_auth_user(self):
        response2 = MyRequests.get("/user/auth",
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})

        Assertions.assert_json_value_by_name(response2,"user_id", self.user_id, "user_id is not the same")

        #assert "user_id" in response2.json(), "There is no user_id in the second response"
        #user_id_2 =  response2.json()["user_id"]
        #assert self.user_id == user_id_2, "user_id is not the same"


    @pytest.mark.parametrize('condition', exclude_params)
    @allure.description("Faild test auth")
    @allure.severity("value = SeverityLevel.BLOCKER")
    @allure.step("Start test")
    def test_negativ_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                     headers={"x-csrf-token": self.token})
        else:
            response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                     cookies={"auth_sid": self.auth_sid})

            Assertions.assert_json_value_by_name(response2, "user_id", 0,  f"user is authorize with condition {condition}")
       #assert "user_id" in response.json(), "There is no user_id"
        #user_id_2 = response2.json()["user_id"]
        #assert user_id_2 == 0, f"user is authorize with condition {condition}"

