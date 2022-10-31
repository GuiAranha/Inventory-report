import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path) as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file))
            else:
                raise ValueError("Arquivo inválido")
