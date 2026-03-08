# Vetor de estoque inicial
estoque = [20, 15, 10, 30, 5]

produtos = ["Produto 0", "Produto 1", "Produto 2", "Produto 3", "Produto 4"]


def exibir_estoque():
    #Exibe a quantidade atual de cada produto no estoque.
    print("\n--- Estoque Atual ---")
    for i in range(len(estoque)):
        print(f"O produto é {produtos[i]}  O estoque doproduto é {estoque[i]} unidades")


def atualizar_venda(indice_produto, quantidade):
    #Atualiza a quantidade em estoque após uma venda.
    estoque[indice_produto] -= quantidade
    print(f"\n{quantidade} unidades de '{produtos[indice_produto]}' vendidas com sucesso.")


def adicionar_estoque(indice_produto, quantidade):
    #Adiciona mais unidades de um produto ao estoque.
    estoque[indice_produto] += quantidade
    print(f"\n{quantidade} unidades de '{produtos[indice_produto]}' adicionadas ao estoque.")


exibir_estoque()

# Exemplo de venda
# Vendendo 5 unidades do Produto 2
atualizar_venda(2, 5)
exibir_estoque()

# Exemplo de venda que deixa o estoque negativo
# Vendendo 25 unidades do Produto 0
atualizar_venda(0, 10)
exibir_estoque()

# Exemplo de adição ao estoque
# Adicionando 10 unidades do Produto 3 (índice 3)
adicionar_estoque(3, 10)
exibir_estoque()

# Exemplo de uma nova venda
# Vendendo 15 unidades do Produto 3 (índice 3) após a adição
atualizar_venda(3, 15)
exibir_estoque()
