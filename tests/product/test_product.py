from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Nescal",
        "Nestle",
        "2023-04-07",
        "2024-04-07",
        "123456789",
        "em local seco e fresco",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Nescal"
    assert product.nome_da_empresa == "Nestle"
    assert product.data_de_fabricacao == "2023-04-07"
    assert product.data_de_validade == "2024-04-07"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "em local seco e fresco"
