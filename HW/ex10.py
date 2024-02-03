import pytest

"""python3 -m pytest -s ex10.py """
class TestEx10:
    def test_ex_10(self):
        phrase = input("Set a phrase less 15 symbols: ")
        expected_symbols = 15
        assert len(phrase) < 15, f"Phrase {phrase} not less {expected_symbols}"