sexo = str(input("Informe seu sexo: [M/F] ")).upper()
while sexo not in "MmFf":
    sexo = str(input("Dado invalido. Informe seu sexo novamente: ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))
