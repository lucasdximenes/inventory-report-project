from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

product_list = [
    {
        "id": "1",
        "nome_do_produto": "Nicotine Polacrilex",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2021-02-18",
        "data_de_validade": "2023-09-17",
        "numero_de_serie": "CR25 1551 4467 2549 4402 1",
        "instrucoes_de_armazenamento": "instrucao 1",
    },
    {
        "id": "2",
        "nome_do_produto": "fentanyl citrate",
        "nome_da_empresa": "Target Corporation",
        "data_de_fabricacao": "2020-12-06",
        "data_de_validade": "2023-12-25",
        "numero_de_serie": "FR29 5951 7573 74OY XKGX 6CSG D20",
        "instrucoes_de_armazenamento": "instrucao 2",
    },
    {
        "id": "3",
        "nome_do_produto": "NITROUS OXIDE",
        "nome_da_empresa": "Galena Biopharma",
        "data_de_fabricacao": "2020-12-22",
        "data_de_validade": "2024-11-07",
        "numero_de_serie": "CZ09 8588 0858 8435 9140 2695",
        "instrucoes_de_armazenamento": "instrucao 3",
    },
    {
        "id": "4",
        "nome_do_produto": "Norepinephrine Bitartrate",
        "nome_da_empresa": "Cantrell Drug Company",
        "data_de_fabricacao": "2020-12-24",
        "data_de_validade": "2025-08-19",
        "numero_de_serie": "MT04 VJPY 0772 3DCE K8U3 WIVL VV3K AEN",
        "instrucoes_de_armazenamento": "instrucao 4",
    },
    {
        "id": "5",
        "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
        "nome_da_empresa": "Moore Medical LLC",
        "data_de_fabricacao": "2021-04-14",
        "data_de_validade": "2025-01-14",
        "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
        "instrucoes_de_armazenamento": "instrucao 5",
    },
    {
        "id": "5",
        "nome_do_produto": "ACETAMINOPHEN, PHENYLEPHRINE HYDROCHLORIDE",
        "nome_da_empresa": "Moore Medical LLC",
        "data_de_fabricacao": "2021-04-14",
        "data_de_validade": "2025-01-14",
        "numero_de_serie": "LV23 ELDS 2GD5 X19P VCSI K",
        "instrucoes_de_armazenamento": "instrucao 5",
    },
]


def test_decorar_relatorio():
    simple_report = SimpleReport()
    colored_report = ColoredReport(simple_report)
    assert colored_report.generate(product_list) == (
        "\033[32mData de fabricação mais antiga:\033[36m 2020-12-06\033[0m]]"
        "\033[32mData de validade mais próxima:\033[36m 2023-09-17\033[0m]]"
        "\033[32mEmpresa com mais produtos:\033[31m Moore Medical LLC\033[0m]]"
    )
