from ..reports.simple_report import SimpleReport
from ..reports.complete_report import CompleteReport
from ..importer.csv_importer import CsvImporter
from ..importer.json_importer import JsonImporter
from ..importer.xml_importer import XmlImporter
import pathlib


class Inventory:
    @staticmethod
    def file_reader(path):
        if pathlib.Path(path).suffix == ".csv":
            return CsvImporter.import_data(path)
        elif pathlib.Path(path).suffix == ".json":
            return JsonImporter.import_data(path)
        elif pathlib.Path(path).suffix == ".xml":
            return XmlImporter.import_data(path)
        else:
            raise ValueError("Invalid file extension")

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
