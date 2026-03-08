soma = 0
v = int(input("Digite o numero de somas: "))
for i in range(0,v):  
    n = int(input(f'Digite um valor {i}: '))
    soma += n
print(f'Soma total é {soma}')
