not1 = float(input("Digite a primeira nota: "))
not2 = float(input("Digite a seguda nota:"))
med = (not1 + not2) / 2
if med <= 5:
    print("Você está REPROVADO.")
elif 5<med<6.9:
    print("Você está de RECUPERAÇÃO.")
else:
    print("Você está APROVADO.")