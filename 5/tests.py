import unittest
import income_service


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.service = income_service.WorkIncome("input.json")

    def test_get_income(self):
        result = self.service.get_income()
        self.assertEqual(result, {'year': 2007, 'month': 'JUNE', 'salary': 133000, 'hour_income': '791.67'})


if __name__ == "__main__":
    unittest.main()