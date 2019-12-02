def lin():
    print("-=" * 13)


def lin2():
    print("-=" * 32)


p18 = ph = pm = 0
while True:
    lin()
    print(" == CADASTRO DE PESSOAS == ")
    lin()

    idade = 0
    sexo = " "

    idade = int(input("Digite a sua idade: "))
    if idade >= 18:
        p18 += 1
    while sexo not in "MF":
        sexo = str(input("Digite seu sexo: [M/F] ")).strip().upper()[0]
    if sexo == "M":
        ph += 1
    if sexo == "F" and idade < 20:
        pm += 1
    perg = " "
    while perg not in "SN":
        perg = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if perg in "Nn":
        break
lin2()
print(f"Total de pessoa(s) com idade maior de 18 anos: {p18}")
lin2()
print(f"Ao todo, tem-se {ph} homem(ns) cadastrado(s)")
lin2()
print(f"E, por fim, existe(m) {pm} mulher(es) com idade menor do que 20 anos.")
lin2()
