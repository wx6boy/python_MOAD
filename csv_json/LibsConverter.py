# title LibsConverter
# description Converter from csv to json, which done with libs
# code
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
