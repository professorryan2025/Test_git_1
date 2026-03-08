n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("\nA soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f}, " .format(s ,sb, m ,d), end="")
print("divisão inteira é {} e a potenciação é {}".format(di, e))