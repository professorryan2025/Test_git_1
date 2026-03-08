numero = [0, 1, 2, 3, 4]

print(f"Minha lista de numeros é: \n {numero}")

posicao_escolhida = int(input("Qual numero você escolhe? (Digite um numero de 0 a 4): "))

if posicao_escolhida >= 0 and posicao_escolhida <= 4:
    numero_escolhido = numero[posicao_escolhida]
    print(f"O numero que você escolheu é: {numero_escolhido}")
else:
    print("Opção invalida, digite um número inteiro entre 0 e 3.")