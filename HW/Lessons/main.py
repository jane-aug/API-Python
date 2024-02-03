from json.decoder import JSONDecodeError
import requests

#простой запрос
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

print("Hello from Jane")

#домашка 4
ex4 = requests.get("https://playground.learnqa.ru/api/get_text")
print(ex4.text)

response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Test"})
print(response.text)

#передача параметров из переменной
payload = {"name": "Test1"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
print(response.text)

#передача параметров напрямую в запросе
response2 = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "Test"})
parsed_json_text = response2.json()
print(parsed_json_text["answer"])

#печать ответа в json если он в таком формате
response3 = requests.get("https://playground.learnqa.ru/api/get_text")
print(response3.text)

try:
    parsed_json_text = response3.json()
    print(parsed_json_text)
except JSONDecodeError:
    print("Response is not a JSON format")
    
#получаем статус код
response5 = requests.post("https://playground.learnqa.ru/api/check_type", data={"name": "Test"})
print(response5.text)
print(response5.status_code)

response6 = requests.post("https://playground.learnqa.ru/api/get_500")
print(response6.text)
print(response6.status_code)

response7 = requests.post("https://playground.learnqa.ru/api/get_50gfg0")
print(response7.text)
print(response7.status_code)

#редиректы и работа с историей перенаправлений
response8 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response8.text)
print(response8.status_code)

response9 = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response9.history[0]
second_response = response9

print(first_response.url)
print(first_response.text)
print(first_response.status_code)

print(second_response.url)
print(second_response.text)
print(second_response.status_code)

#работа с хедерами
headears = {"name": "Test1"}
response10 = requests.post("https://playground.learnqa.ru/api/show_all_headers", headers = headears)
print(response10.text)
print(response10.headers)


#работа с куки
payload = {"login": "secret_login", "password": "secret_pass"}

response11 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data= payload)

cookie_value = response11.cookies.get('auth_cookie')
cookies = {}
if cookies is not None:
   cookies.update({'auth_cookie':cookie_value})


print(response11.url)
print(response11.text)
print(response11.status_code)
print(response11.headers)
print(dict(response11.cookies))

response12 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)

print(response12.text)
