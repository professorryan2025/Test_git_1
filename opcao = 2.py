opcao = int(input("Digite uma opção entre 1,2 e 3: "))

match opcao:
    case 1:
        print("Você escolheu a opção 1.")
    case 2:
        print("Você escolheu a opção 2.")
    case 3:
        print("Você escolheu a opção 3.")
    case _:
        print("Opção inválida.")