import json
from random import randint


class WorkingDays:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def days_amount(self):
        return randint(20,23)


class WorkIncome:
    def __init__(self, filename):
        self.filename = filename

    def get_income(self):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        work_days = WorkingDays(data['year'], data['month'])
        days_amount = work_days.days_amount()
        data['hour_income'] = "{:.2f}".format(data['salary'] / (8 * days_amount))
        return data

    def make_json(self, data):
        data = json.dumps(data)
        data = self.get_income()
        with open('output.json', 'w') as f:
            f.write(data)