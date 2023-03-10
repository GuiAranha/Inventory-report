from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "nome_do_produto",
        "nome_da_empresa",
        "30-10-2022",
        "31-10-2022",
        "numero_de_serie",
        "instrucoes_de_armazenamento",
    )
    assert product.id == 1
    assert product.nome_do_produto == "nome_do_produto"
    assert product.nome_da_empresa == "nome_da_empresa"
    assert product.data_de_fabricacao == "30-10-2022"
    assert product.data_de_validade == "31-10-2022"
    assert product.numero_de_serie == "numero_de_serie"
    assert product.instrucoes_de_armazenamento == "instrucoes_de_armazenamento"
