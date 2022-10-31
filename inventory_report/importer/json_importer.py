import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            if path.endswith(".json"):
                return list(json.load(file))
            else:
                raise ValueError("Arquivo inválido")
