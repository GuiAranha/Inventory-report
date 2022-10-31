from collections import Counter
from datetime import datetime


class SimpleReport:

    @classmethod
    def get_newest_date(cls, list):
        return min(
            datetime.fromisoformat(item["data_de_validade"]).date()
            for item in list
            if datetime.fromisoformat(item["data_de_validade"])
            > datetime.now()
        )

    @classmethod
    def get_oldest_date(cls, list):
        return min(
            datetime.fromisoformat(item["data_de_fabricacao"]).date()
            for item in list
        )

    @classmethod
    def get_company_more_products(cls, list):
        return Counter(
            [item["nome_da_empresa"] for item in list]
        ).most_common()[0][0]

    @classmethod
    def generate(cls, list):
        newest = SimpleReport.get_newest_date(list)
        oldest = SimpleReport.get_oldest_date(list)
        company = SimpleReport.get_company_more_products(list)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {newest}\n"
            f"Empresa com mais produtos: {company}"
        )
