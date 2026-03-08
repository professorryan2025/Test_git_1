def somar (A , B):
    C=[]

    nLinhaA, nLinhaB = len(A), len(B)
    nColuA, nColuB = len(A[0]), len(B[0])

    if (nLinhaA == nLinhaB) and (nColuA == nColuB ):
        for i in range(nLinhaA):
            linha = [0]*nColuA
            linha = [0]*nColuA
            C.append(linha)
            for j in range(nColuA):
                C[i][j] = A[i][j] + B [i][j]
            
    else:
        print('Matrizes não tem a mesma ordem')
    
    return C

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
