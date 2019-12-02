def lin():
    print("-=" * 16)


lin()
print(" == ANÁLISE DE DADOS + LISTA == ")
lin()

temporaria = list()
principal = list()
maior = menor = 0

while True:
    temporaria.append(str(input("Digite seu nome: ")))
    temporaria.append(float(input("Digite seu peso: ")))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break
lin()
print(f"Ao todo, {len(principal)} foi(ram) cadastrada(s).")
print(f"O maior peso regitrado foi {maior}Kg, ", end="de ")
for p in principal:
    if p[1] == maior:
        print(f"{p[0]}")
print(f"O menor peso regitrado foi {menor}Kg, ", end="de ")
for p in principal:
    if p[1] == menor:
        print(f"{p[0]}")
