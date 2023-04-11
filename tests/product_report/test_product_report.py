from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "Sabão em pó",
        "Omo",
        "2023-03-13",
        "2024-03-13",
        "123456789",
        "em local seco e arejado",
    )
    assert (
        product.__repr__() == "O produto Sabão em pó"
        " fabricado em 2023-03-13"
        " por Omo com validade"
        " até 2024-03-13"
        " precisa ser armazenado em local seco e arejado."
    )
