import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            if path.endswith(".xml"):
                return xmltodict.parse(file.read())["dataset"]["record"]
            else:
                raise ValueError("Arquivo inválido")
