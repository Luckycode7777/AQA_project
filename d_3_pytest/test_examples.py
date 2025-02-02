class TestExamples:
    def test_1(self):
        a = 1
        b = 2
        expected_res = 3
        assert a + b == expected_res, f'Сумма не верная {expected_res}'

    def test_2(self):
        a = 5
        b = 5
        expected_res = 10
        assert a + b == 11, f'Сумма не верная. Должна быть >>> {expected_res}'
