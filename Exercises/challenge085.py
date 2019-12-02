def lin():
    print("-=" * 16)


lin()
print(" == LISTA COM PARES E ÍMPARES == ")
lin()

pares = []
impares = []

for n in range(1,8):
    num = int(input(f"Digite o {n}° valor: "))
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 == 1:
        impares.append(num)

pares.sort()
impares.sort()

print(f"Os valores pares são {pares}")
print(f"Os valores ímpares são {impares}")
