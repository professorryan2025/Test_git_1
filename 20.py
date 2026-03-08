while True:
    dados = range(int(input("Digite o numero de processos: ")))

    if dados:
        print("\nPROCESSAMENTO Dados encontrados. Iniciando o processamento...")
        for n in dados:
            print(f"    - Processando o registro: {n}")
        break
    else:
        print("\nConjunto de dados vazio. Nenhum dado a ser processado.")   

print("Fim programa")
