idade = int(input("Digite a sua idade: ")) 

if idade  <=12:
    print("\nVoce é uma criança")
elif idade < 18:
    print('\nVoce é adolecente')
elif idade < 60:
    print ('\nVoce é adulto')    
else:
    print("\nVoce é idoso")