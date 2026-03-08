
valor_compra = float(input('Digite o valor total da compra: '))
valor_original = valor_compra
fidelidade = input('Possui fidelidade? sim/nao ')

if valor_compra > 0 and valor_compra < 50:
    print(f'\nSem desconto: {valor_compra}')

elif valor_compra >= 50 and valor_compra <= 100:
    desconto = (5 * valor_compra)/100
    valor_compra = valor_compra - desconto
    print(f'\nO valor original é {valor_original} \nCom 5% de desconto: {valor_compra}')

elif valor_compra > 100 and valor_compra <=200:
    desconto = (10 * valor_compra)/100
    valor_compra = valor_compra - desconto
    print(f'\nO valor original é {valor_original} \nCom 10% de desconto: {valor_compra}')

elif valor_compra > 200:
    desconto = (15 * valor_compra)/100
    valor_compra = valor_compra - desconto
    print(f'\nO valor original é {valor_original} \nCom 15% de desconto: {valor_compra}')
else:
    print('\nValor invalido')

if fidelidade == ("sim") and valor_compra >= 0:
    desconto = (5 * valor_compra)/100
    valor_compra = valor_compra - desconto
    print(f'\nSeu desconto com a fidelidade é: {valor_compra}') 
else:
    print('Sem fidelidade')