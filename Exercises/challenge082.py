def lin():
    print("-=" * 14)



lin()
print(" == DADOS PARA UMA LISTA == ")
lin()

dados = list()
pares = list()
impares = list()

while True:
    dados.append(int(input("Digite um número: ")))
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break

for i, v in enumerate(dados):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
lin()
print(f"Os números digitados foram: {dados}")

print(f"Os números pares digitados foram: {pares}")

print(f"Os números ímpares digitados foram: {impares}")
