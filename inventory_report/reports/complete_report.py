from collections import defaultdict
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate_report(data):
        stock_of_each_company = defaultdict(int)

        for product in data:
            company = product["nome_da_empresa"]
            stock_of_each_company[company] += 1

        report = "\n".join(
            [
                f"- {company}: {stock}"
                for company, stock in stock_of_each_company.items()
            ]
        )

        return report + "\n"

    @staticmethod
    def generate(data: list[dict]) -> str:
        report = SimpleReport.generate(data)
        report += "\n"
        report += "Produtos estocados por empresa:\n"
        report += CompleteReport.generate_report(data)
        return report
