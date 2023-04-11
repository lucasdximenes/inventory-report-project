import pathlib
import xmltodict
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if pathlib.Path(path).suffix != ".xml":
            raise ValueError("Arquivo inválido")

        with open(path, encoding="utf8") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
