from  lib.assertions import Assertions
from lib.base_case import BaseCase
import requests
import pytest
class TestUserRegistry(BaseCase):
    """  python3 -m pytest -s tests/test_user_register.py """
    """  python3 -m pytest -s tests/test_user_register.py - k create_user_successffuly"""

    invalid_data = [
        {'password': '12345', 'username': 'test', 'firstName': 'firstName', 'lastName': 'test'},
        {'email': 'zhenya_shalanova@mail.ru', 'username': 'test', 'firstName': 'firstName', 'lastName': 'test'},
        {'email': 'zhenya_shalanova@mail.ru', 'password': '12345', 'firstName': 'firstName', 'lastName': 'test'},
        {'email': 'zhenya_shalanova@mail.ru', 'password': '12345', 'username': 'test', 'lastName': 'test'},
        {'email': 'zhenya_shalanova@mail.ru', 'password': '12345', 'username': 'test', 'firstName': 'firstName'}
    ]

    def test_create_user_successffuly(self):
        data = self.prepare_reg_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_compare_status_code(response,200)
        Assertions.assert_json_has_key(response, "id")


    def test_register_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_reg_data(email)
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_compare_status_code(response,400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists" , f"Unexpected response content '{response.content}'"

    #ex15

    def test_register_user_with_error_email(self):
        email = 'vinkotovexample.com'
        data = self.prepare_reg_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_compare_status_code(response,400)
        Assertions.assert_compare_response_text(response, "Invalid email format")
    def test_register_user_with_short_username(self):
        data = {
            'email': 'zhenya_shalanova@mail.ru',
            'password': '12345',
            'username': '1',
            'firstName': 'learnqa',
            'lastName': 'learnqa'
            }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_compare_status_code(response,400)
        Assertions.assert_compare_response_text(response, "The value of 'username' field is too short" )

    def test_regiister_user_with_long_first_name(self):
        firstName = 'Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи Абдурахмангаджи'
        data = {
            'email': 'zhenya_shalanova@mail.ru',
            'password': '12345',
            'username': 'test',
            'firstName': firstName,
            'lastName': 'test'
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_compare_status_code(response,400)
        Assertions.assert_compare_response_text(response,"The value of 'firstName' field is too long")

    @pytest.mark.parametrize('data', invalid_data)
    def test_register_user_without_1_field(self, data):
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_compare_status_code(response,400)
        assert response.text.startswith("The following required params are missed:")




        #print(response.url, response.text, response.content, response.status_code, response.cookies, sep='\n')

