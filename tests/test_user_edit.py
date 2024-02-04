import requests
import pytest
from lib.assertions import Assertions
from lib.base_case import BaseCase


class TestUserEdit(BaseCase):
    def test_user_edit_just_created(self):

        #REGISTER
        reg_data = self.prepare_reg_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data = reg_data)
        Assertions.assert_compare_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = reg_data['email']
        first_name = reg_data['firstName']
        password = reg_data['password']
        user_id = self.get_json_value(response, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        #CHANGE

        new_name = "Lora"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name})
        Assertions.assert_compare_status_code(response3, 200)

        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Name not changed")

    #ex17

    def test_user_edit_without_authorize(self):
        new_name = "Lora"
        response = requests.put(f"https://playground.learnqa.ru/api/user/90369",
                                 data={"firstName": new_name})
        Assertions.assert_compare_status_code(response, 400)
        Assertions.assert_compare_response_text(response, "Auth token not supplied")


    def test_user_edit_with_foregin_token(self):

        #REGISTER
        reg_data = self.prepare_reg_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data = reg_data)
        print("REGISTER")
        print(response.url, response.text, response.content, response.status_code, response.cookies, sep='\n')

        Assertions.assert_compare_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = reg_data['email']
        first_name = reg_data['firstName']
        password = reg_data['password']
        user_id = self.get_json_value(response, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        print("LOGIN")
        print(response2.url, response2.text, response2.content, response2.status_code, response2.cookies, sep='\n')

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        #CHANGE

        new_name = "Lora1"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/90369",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name})
        Assertions.assert_compare_status_code(response3, 200)

        print("CHANGE")
        print(response3.url, response3.text, response3.content, response3.status_code, response3.cookies, sep='\n')


        #GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/90369",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        print(response4.url, response4.text, response4.content, response4.status_code, response4.cookies, sep='\n')

        Assertions.assert_json_has_key(response4, "firstName")
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Name not changed")

    def test_user_edit_just_created_with_wrong_email(self):

        #REGISTER
        reg_data = self.prepare_reg_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data = reg_data)
        Assertions.assert_compare_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = reg_data['email']
        first_name = reg_data['firstName']
        password = reg_data['password']
        user_id = self.get_json_value(response, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        #CHANGE

        new_email = "Lora"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email})
        Assertions.assert_compare_status_code(response3, 400)
        Assertions.assert_compare_response_text(response3, "Invalid email format")

    def test_user_edit_just_created_with_shhort_name(self):
        # REGISTER
        reg_data = self.prepare_reg_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=reg_data)
        Assertions.assert_compare_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

        email = reg_data['email']
        first_name = reg_data['firstName']
        password = reg_data['password']
        user_id = self.get_json_value(response, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")
        user_id = self.get_json_value(response2, "user_id")

        # CHANGE

        new_name = "1"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name})
        Assertions.assert_compare_status_code(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName", "Name changed")






