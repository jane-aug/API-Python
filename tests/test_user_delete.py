import requests
from lib.assertions import Assertions
from lib.base_case import BaseCase

#ex18
class TestUserDelete(BaseCase):
    def test_user_delete(self):
        # LOGIN
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id = self.get_json_value(response, "user_id")

        # DELETE

        response2 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        Assertions.assert_compare_status_code(response2, 400)
        Assertions.assert_compare_response_text(response2, "Please, do not delete test users with ID 1, 2, 3, 4 or 5.")

    def test_user_delete_just_created_and_check_data(self):
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

            # DELETE
            response3 = requests.delete(f"https://playground.learnqa.ru/api/user/{user_id}",
                                        headers={"x-csrf-token": token},
                                        cookies={"auth_sid": auth_sid})
            Assertions.assert_compare_status_code(response3, 200)

            # GET
            response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                     headers={"x-csrf-token": token},
                                     cookies={"auth_sid": auth_sid})

            Assertions.assert_compare_status_code(response4, 404)
            Assertions.assert_compare_response_text(response4,"User not found")

    def test_user_delete_another_user(self):
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

        # DELETE
        response3 = requests.delete(f"https://playground.learnqa.ru/api/user/90369",
                                    headers={"x-csrf-token": token},
                                    cookies={"auth_sid": auth_sid})
        # GET
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/90369",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        Assertions.assert_compare_status_code(response3, 200)

