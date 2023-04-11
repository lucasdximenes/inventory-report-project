import csv
from .importer import Importer
import pathlib


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if pathlib.Path(path).suffix != ".csv":
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            return list(reader)
