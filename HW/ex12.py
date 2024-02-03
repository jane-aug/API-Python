import requests

"""python3 -m pytest -s ex12.py """

class TestEx12:
    def test_ex11(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        print(response.url, dict(response.headers), response.text, response.status_code, dict(response.cookies), sep='\n')


        # сохраняем хедер для проверки
        headers_value = response.headers.get('x-secret-homework-header')

        assert response.status_code == 200, "Wrong response code"

        expected_headers = "Some secret value"

        assert headers_value == expected_headers, "Response headers not equel expexcted"