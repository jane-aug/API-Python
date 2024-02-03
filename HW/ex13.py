import requests
import pytest
from json.decoder import JSONDecodeError


''' python3 -m pytest -s ex13.py '''
class TestEx13:
   user_agents = [
      'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
      'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
      'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
      'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
   ]

   expected_values = [
      {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
      {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
      {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
      {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
      {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
   ]

   @pytest.mark.parametrize('user_agents, expected_values', list(zip(user_agents, expected_values)))
   def test_ex13(self, user_agents, expected_values):
      url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
      response = requests.get(url, headers={"User-Agent": user_agents})

      #проверяем статус код
      assert response.status_code == 200, "Wrong response code"

      #проверяем что в ответе есть нужные поля
      parsed_json_text = response.json()
      assert "platform" in parsed_json_text, "There is no field 'platform' in the response"
      assert "browser" in parsed_json_text, "There is no field 'browser' in the response"
      assert "device" in parsed_json_text, "There is no field 'device' in the response"

      print(parsed_json_text, expected_values,  sep='\n')
      print("---")
      #сохраняем ожидаемые поля по отдельности
      expected_platform = expected_values.get('platform')
      expected_browser = expected_values.get('browser')
      expected_device = expected_values.get('device')

      #сохраняем получаемые поля по отдельности
      recived_platform = parsed_json_text.get('platform')
      recived_browser = parsed_json_text.get('browser')
      recived_device = parsed_json_text.get('device')


      assert expected_platform == recived_platform , f"recived platform '{recived_platform}' in the response is not correct. Expected '{expected_platform}'"
      assert expected_browser == recived_browser , f"recived browser '{recived_browser}' in the response is not correct. Expected '{expected_browser}'"
      assert expected_device == recived_device , f"recived device '{recived_device}' in the response is not correct. Expected '{expected_device}'"
