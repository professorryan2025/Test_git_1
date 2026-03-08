
numeros = []

print("Por favor, digite 5 números:")
for i in range(5):
    try:
        num = float(input(f"Digite o {i+1}º número: "))
        numeros.append(num)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        i -= 1

soma = 0
for num in numeros:
    soma += num

media = soma / len(numeros)

print("\n--- Resultados ---")
print(f"Os números digitados foram: {numeros}")
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}") 