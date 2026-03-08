v = int(input('Digite um numero: '))

# Cria um vetor N com 10 posições
n = [0] * 11

# Coloca o valor lido na primeira posição do vetor
n[0] = v 

# Preenche as posições subsequentes com o dobro do valor da posição anterior
for i in range(1, 11):
    n[i] = n[i-1] * 2

# Exibe o vetor
for i in range(11):
    print(f"Numero [{i}] = {n[i]}")


