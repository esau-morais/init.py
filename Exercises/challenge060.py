def lin():
    print("-=" * 15)


lin()
print("  == Cálculo de Fatorial == ")
lin()

import math
num = int(input("Digite um número: "))
fat = math.factorial(num)
cont = num
print(f"{num}! = ", end="")
while cont > 0:
    print("{}".format(cont), end="")
    print(" x " if cont > 1 else " = ", end="")
    cont -= 1
print(f"{fat}")
