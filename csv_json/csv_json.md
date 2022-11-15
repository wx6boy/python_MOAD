# csv_json

+ [LibsConverter](#LibsConverter)
+ [SelfConverter](#SelfConverter)
+ [TestCsvJsonConverter](#TestCsvJsonConverter)

## LibsConverter

 Converter from csv to json, which done with libs

```python
import json
import csv


class LibConverter:

    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def read(self):
        with open(self.csv_path, "r", newline="") as f:
            return list(csv.DictReader(f))

    def write(self, data):
        data = json.dumps(data)
        with open(self.json_path, "w") as f:
            f.write(data)
        print("Data was converted successfully.")
        return data


def main():
    csv_path = "./input.csv"
    json_path = "./output.json"

    converter = LibConverter(csv_path=csv_path, json_path=json_path)

    data = converter.read()
    converter.write(data)


if __name__ == "__main__":
    main()

```

## SelfConverter

 Self made converter class and additional functions

```python
def preprocess_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(title, values):
    result_data = []
    for current_values in values:
        current_dict = dict(zip(title, current_values.split(",")))
        pretty_line = "{"
        current_list = []
        for key in current_dict:
            current_list.append('"{key}": "{value}"'.format(key=key, value=current_dict[key]))

        pretty_line += ", ".join(current_list) + "}"
        result_data.append(pretty_line)

    result_data = "[" + ", ".join(result_data) + "]"
    return result_data


class SelfConverter:
    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def read_data(self):
        with open(self.csv_path, "r", newline="") as f:
            content = f.read().splitlines()
            f.close()
        return preprocess_data(content)

    def write_data(self, data):
        with open(self.json_path, "w") as f:
            f.write(data)
        print("Data was converted successfully.")
        return data


def main():
    csv_path = "./input.csv"
    json_path = "./output.json"

    converter = SelfConverter(csv_path, json_path)
    title, values = converter.read_data()

    data = convert_row_to_pretty_json(title, values)
    converter.write_data(data)


if __name__ == "__main__":
    main()

```

## TestCsvJsonConverter

 Unit tests for csv to json converters

```python
from LibsConverter import LibConverter
from SelfConverter import SelfConverter, convert_row_to_pretty_json
import unittest
import json


class TestCsvJsonConverter(unittest.TestCase):

    csv_path = "./input.csv"
    json_path = "./output.json"
    self_converter = SelfConverter(csv_path, json_path)
    lib_converter = LibConverter(csv_path, json_path)

    def test_read(self):
        self.assertTrue(self.self_converter.read_data())
        self.assertTrue(self.lib_converter.read())

    def test_write(self):
        data = self.lib_converter.read()
        written_data = self.lib_converter.write(data)

        title, values = self.self_converter.read_data()

        data = convert_row_to_pretty_json(title, values)
        check_data = self.self_converter.write_data(data)
        self.assertEqual(written_data, check_data)

    def test_row_to_pretty(self):
        data = self.lib_converter.read()
        data_lib = json.dumps(data)

        title, values = self.self_converter.read_data()
        data_self = convert_row_to_pretty_json(title, values)
        self.assertEqual(data_lib, data_self)



if __name__ == '__main__':
    unittest.main()



```
