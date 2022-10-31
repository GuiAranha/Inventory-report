import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def open_file(cls, path):
        with open(path) as file:
            if path.endswith(".csv"):
                products = list(csv.DictReader(file))
            elif path.endswith(".json"):
                products = list(json.load(file))
            elif path.endswith(".xml"):
                products = xmltodict.parse(file.read())["dataset"]["record"]
            return products

    @classmethod
    def import_data(cls, path, type):
        data = Inventory.open_file(path)
        if type == "completo":
            return CompleteReport.generate(data)
        if type == "simples":
            return SimpleReport.generate(data)
