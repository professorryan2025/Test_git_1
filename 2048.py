def somar_matrizes_loop(A, B):
    """Soma duas matrizes (listas de listas) usando loops aninhados."""
    
    # 1. Obter dimensões (número de linhas e colunas)
    linhas = len(A)
    colunas = len(A[0])

    # 2. Criar uma matriz de resultado preenchida com zeros
    # A nova matriz deve ter as mesmas dimensões
    C = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # 3. Iterar sobre cada elemento e realizar a soma
    for i in range(linhas):
        for j in range(colunas):
            C[i][j] = A[i][j] + B[i][j]
            
    return C

# Definição das matrizes como listas de listas (puro Python)
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15]
]

matriz_soma = somar_matrizes_loop(matriz_a, matriz_b)

print("Matriz Soma (usando loops):")
for linha in matriz_soma:
    print(linha)