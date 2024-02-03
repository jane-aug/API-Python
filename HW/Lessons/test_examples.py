class TestExample:

    """  python3 -m pytest test_examples.py -k "test_check_math" """
    def test_check_math(self):
        a = 5
        b = 9
        expected_sum = 14
        assert a + b == expected_sum, f"Sum of var is not equel to {expected_sum}"

    def test_check_math2(self):
            a = 5
            b = 11
            expected_sum = 14
            assert a + b == expected_sum, f"Sum of var is not equel to {expected_sum}"
