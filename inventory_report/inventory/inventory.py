import csv
import json
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import pathlib
import xmltodict


class Inventory:
    @staticmethod
    def csv_reader(path):
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def json_reader(path):
        with open(path, encoding="utf8") as file:
            return json.load(file)

    @staticmethod
    def xml_reader(path):
        with open(path, encoding="utf8") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @staticmethod
    def file_reader(path):
        if pathlib.Path(path).suffix == ".csv":
            return Inventory.csv_reader(path)
        elif pathlib.Path(path).suffix == ".json":
            return Inventory.json_reader(path)
        elif pathlib.Path(path).suffix == ".xml":
            return Inventory.xml_reader(path)
        else:
            raise ValueError("File is not a valid format")

    @staticmethod
    def import_data(path, type):
        data = Inventory.file_reader(path)

        if type == "simples":
            report = SimpleReport.generate(data)
        elif type == "completo":
            report = CompleteReport.generate(data)
        else:
            raise ValueError("Invalid report type")

        return report
