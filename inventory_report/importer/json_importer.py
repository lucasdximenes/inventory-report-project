import json
import pathlib
from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if pathlib.Path(path).suffix != ".json":
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf8") as file:
            return json.load(file)
