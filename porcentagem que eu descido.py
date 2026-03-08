
valor_produto = float(input("Digite o valor do produto: R$ "))

percentual_desconto = float(input("Digite a porcentagem de desconto (ex: 10 para 10%): "))

valor_desconto = valor_produto * (percentual_desconto / 100)

valor_final = valor_produto - valor_desconto

print("\n--- Resumo da Compra ---")
print(f"Valor original do produto: R$ {valor_produto}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto}")
print("--------------------------")
print(f"Valor final a pagar: R$ {valor_final}")