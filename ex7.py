import requests
#запрос без параметра
response = requests.get("https://playground.learnqa.ru/api/compare_query_type")
print(response.url,response.text,response.status_code)

#запрос иного типа HEAD
response = requests.head("https://playground.learnqa.ru/api/compare_query_type", params={"method": "HEAD"})
print(response.url,response.text,response.status_code)

#запросы с параметрами методамии POST, GET, PUT, DELETE

response = requests.get("https://playground.learnqa.ru/api/compare_query_type", params={"method": "GET"})
print(response.url,response.text,response.status_code)

response = requests.post("https://playground.learnqa.ru/api/compare_query_type", data={"method": "POST"})
print(response.url,response.text,response.status_code)

response = requests.put("https://playground.learnqa.ru/api/compare_query_type", data={"method": "PUT"})
print(response.url,response.text,response.status_code)

response = requests.delete("https://playground.learnqa.ru/api/compare_query_type", data={"method": "DELETE"})
print(response.url,response.text,response.status_code)

parameters_methods_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]
for param in parameters_methods_list:

        result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Метод GET с {param} получил ответ {result.text}")

        result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метод POST с {param} получил ответ {result.text}")

        result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метол PUT с {param} получил ответ {result.text}")

        result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метод DELETE с {param} получил ответ{result.text}")

#Метод DELETE с {'method': 'GET'} получил ответ{"success":"!"}

