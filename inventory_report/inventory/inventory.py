import csv
from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
import pathlib


class Inventory:
    @staticmethod
    def csv_reader(path):
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def file_reader(path):
        if pathlib.Path(path).suffix == ".csv":
            return Inventory.csv_reader(path)
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
