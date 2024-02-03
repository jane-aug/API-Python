import requests

"""python3 -m pytest -s ex11.py """

class TestEx11:
    def test_ex11(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        print(response.url, response.text, response.status_code, dict(response.cookies), sep='\n')


        # сохраняем куку для проверки
        cookie_value = response.cookies.get('HomeWork')

        assert response.status_code == 200, "Wrong response code"

        expected_cookies = "hw_value"

        assert cookie_value == expected_cookies, "Response cookies not equel expexcted"