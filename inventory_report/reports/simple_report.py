from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        oldest_manufacturing_date = min(
            datetime.strptime(product["data_de_fabricacao"], "%Y-%m-%d")
            for product in data
        ).date()

        nearest_expiration_date = min(
            datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            for product in data
            if datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            > datetime.now()
        ).date()

        company_with_most_products = max(
            set(product["nome_da_empresa"] for product in data),
            key=lambda company: sum(
                1 for product in data if product["nome_da_empresa"] == company
            ),
        )

        report = (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
        )
        report += f"Data de validade mais próxima: {nearest_expiration_date}\n"
        report += f"Empresa com mais produtos: {company_with_most_products}"

        return report
