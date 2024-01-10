import requests
response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)

print("Hello from Jane")

ex4 = requests.get("https://playground.learnqa.ru/api/get_text")
print(ex4.text)