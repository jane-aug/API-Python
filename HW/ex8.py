import requests
import json
import time

#первый запрос на начало работы
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.url,response.text,response.status_code, sep = '\n')

#парсим ответ
obj = json.loads(response.text)
token = obj['token']
seconds = obj['seconds']

#делаем запрос во время обработки задачи
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
print(response1.url,response1.text,response1.status_code , sep = '\n')
obj1 = json.loads(response1.text)
status = obj1['status']
if status == "Job is NOT ready":
    print("Статус коррректный " + status)
else:     print("Статус НЕ коррректный  " + status)


#ждем
time.sleep(seconds)


#делаем запрос после обработки задачи
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job",  params={"token": token})
print(response2.url,response2.text,response2.status_code, sep = '\n')
obj2 = json.loads(response2.text)
status1 = obj2['status']
result = obj2['result']
if (status1 == "Job is ready" and  result != None):
    print("Статус коррректный  " + status1)
else:     print("Статус НЕ коррректный " + status1)
