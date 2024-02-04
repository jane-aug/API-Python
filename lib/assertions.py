from requests import Response
import json
class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_massage):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False,  f"Response is not in JSON format. Response text: '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_massage

    @staticmethod
    def assert_compare_response_text(response: Response, expected_value):
        try:
            response_text = response.text
        except:
            response.text == 0, f"Response text is empty"
        assert  response_text ==  expected_value, f"Unexpected text :'{response_text}', expexted:'{expected_value}'"


    @staticmethod
    def assert_compare_status_code(response: Response, expected_value):
        assert response.status_code == expected_value, f"Unexpected Status Code '{response.status_code}', expexted:'{expected_value}'"


    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False,  f"Response is not in JSON format. Response text: '{response.text}'"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text: '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text: '{response.text}'"

        assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But is present"

    @staticmethod
    def assert_json_has_no_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text: '{response.text}'"
        for name in names:
            assert name not in response_as_dict, f"Response JSON shouldn't have key '{name}'. But is present"