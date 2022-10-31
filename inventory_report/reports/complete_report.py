from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def products_by_company(cls, list):
        data = ""
        products = Counter(
            [item["nome_da_empresa"] for item in list]
        )
        for company, quantity in products.items():
            data = data + f"- {company}: {quantity}\n"
        return data

    @classmethod
    def generate(cls, list):
        products = CompleteReport.products_by_company(list)

        return (
            super().generate(list)
            + "\nProdutos estocados por empresa:\n" + products
        )
