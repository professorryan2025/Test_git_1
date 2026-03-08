def somar (A , B):
    S = []

    nLinhaA= len(A)
    nColuA = len(A[0])

    for i in range(nLinhaA):
        linha = [0]*nColuA
        S.append(linha)
        for j in range(nColuA):
            S[i][j] = A[i][j] + B [i][j]

    return S

matriz = ([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])

matriz2= ([[0,0,0],
          [0,0,0],
          [0,0,0]])

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha] [coluna] = int(input(f"Digite um valor para linha e coluna {linha}, {coluna} da matriz 1: "))
print('-' * 30)

for linha in range(0,3):
    for coluna in range(0,3):
        matriz2[linha] [coluna] = int(input(f"Digite um valor para linha e coluna {linha}, {coluna} da matriz 2: "))
print('-' * 30)

matriz_soma = somar(matriz, matriz2)

print('A matriz 1 é: ')
for linha in matriz:
    print(linha)

print('-' * 30)

print('A matriz 2 é: ')
for linha in matriz2:
    print(linha)

print('-' * 30)

print("A Matriz soma é: ")
for linha in matriz_soma:
    print(linha)

  
