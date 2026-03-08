def mover_esquerda(matriz):

    nova_matriz = []

    # Processa cada linha individualmente
    for linha in matriz:
        # 1. Compressão (Move todos os números != 0 para a esquerda)
        # Cria uma nova lista apenas com os números diferentes de zero (não-zeros)
        nao_zeros = [num for num in linha if num != 0]

        # Preenche com zeros à direita até ter 4 elementos
        linha_comprimida = nao_zeros + [0] * (4 - len(nao_zeros))

        # 2. Fusão (Combina números adjacentes iguais da esquerda para a direita)
        for i in range(3):  # Percorre os índices 0, 1, 2
            if linha_comprimida[i] != 0 and linha_comprimida[i] == linha_comprimida[i+1]:
                # Combina o par: dobra o valor do primeiro elemento
                linha_comprimida[i] *= 2
                # Zera o segundo elemento (o que foi combinado)
                linha_comprimida[i+1] = 0

        # 3. Compressão final (Move os não-zeros restantes para a esquerda novamente)
        # Refaz a compressão após a fusão
        nao_zeros_finais = [num for num in linha_comprimida if num != 0]

        # Preenche com zeros à direita
        linha_final = nao_zeros_finais + [0] * (4 - len(nao_zeros_finais))

        nova_matriz.append(linha_final)

    return nova_matriz


matriz_inicial = [
    [2, 0, 2, 4],  # Caso 1: Compressão + Fusão (2,2)
    [4, 4, 8, 8],  # Caso 2: Dupla Fusão (4,4) e (8,8)
    [2, 2, 4, 4],  # Caso 3: Dupla Fusão seguida de Compressão (2,2) e (4,4)
    [0, 2, 0, 2]   # Caso 4: Compressão inicial + Fusão (2,2)
]

print("Matriz Inicial:")
for linha in matriz_inicial:
    print(linha)

matriz_resultado = mover_esquerda(matriz_inicial)

print("\nMatriz Após Movimento para a Esquerda:")
for linha in matriz_resultado:
    print(linha)