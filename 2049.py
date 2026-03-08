
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

matriz1= [[1,2,3],
          [3,7,2],
          [8,5,4]]

matriz2= [[9,2,3],
          [3,6,2],
          [5,4,6]]

matriz_soma = somar(matriz1, matriz2)

print('A matriz 1 é: ')
for linha in matriz1:
    print(linha)

print('-' * 30)

print('A matriz 2 é: ')
for linha in matriz2:
    print(linha)

print('-' * 30)

print("A Matriz soma é: ")
for linha in matriz_soma:
    print(linha)

  
