valor_compra = float(input('Digite o valor total da compra: '))
desconto : int


desconto = (5 * valor_compra)/100
valor_compra = valor_compra - desconto

print(f'\n5% de desconto: {valor_compra}')