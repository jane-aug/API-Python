import requests
from lib.assertions import Assertions
from lib.base_case import BaseCase

class TestUserGer(BaseCase):
    def test_get_user_details_not_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        Assertions.assert_json_has_key( response,"username")
        Assertions.assert_json_has_no_key(response,"email")
        Assertions.assert_json_has_no_key(response,"firstName")
        Assertions.assert_json_has_no_key(response, "lastName")

    def test_get_user_details_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id = self.get_json_value(response, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}", headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})
        expected_fields = ["username","email" ,"firstName","lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields )

    #ex16
    def test_get_user_details_as_diff_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id = self.get_json_value(response, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/90369", headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        unexpected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_key(response2, "username")
        Assertions.assert_json_has_no_keys(response2, unexpected_fields)



