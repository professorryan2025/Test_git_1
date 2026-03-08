frutas = ["Maçã", "Banana", "Laranja", "Uva"]

print(f"Minha lista de frutas é: \n {frutas}")

posicao_escolhida = int(input("Qual fruta você quer? (Digite a posição de 0 a 3): "))

if posicao_escolhida >= 0 and posicao_escolhida <= 3:
    fruta_escolhida = frutas[posicao_escolhida]
    print(f"A fruta que você escolheu é: {fruta_escolhida}")
else:
    print("Opção invalida, digite um número inteiro entre 0 e 3.")