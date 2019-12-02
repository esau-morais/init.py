# Tupla 1
lanche = ("Biscoito", "Suco")
print(lanche)

# Tupla 1.1
lanche = ("Salgado", "Suco")
print(lanche[0]) and print(lanche[-2])
print(lanche[1]) and print(lanche[-1])

# Tupla 1.2
lanche = ("Salgado", "Suco")
print("O seu lanche tem", len(lanche), "comidas")

# Tupla 1.3
lanche = ("Salgado", "Suco")
for l in lanche:
    print(f"Você comeu {l}")
resp = input("Você está satisfeito? [S/N]").upper()
if resp == "N":
    mais = input("O que você deseja mais? ")
    print("Ok, seu pedido será efetuado. Espere, por favor.")
else:
    print("Que bom que você ficou satisfeito!")

# Tupla 1.4
lanche = ("Salgado", "Suco")
for c in range(0, len(lanche)):
    print(f"Você comeu {lanche[c]}")
print("Espero que tenha ficado satisfeito.")

# Tupla 1.5
lanche = ("Salgado", "Suco")
for c, p in enumerate(lanche):
    print(f"Eu vou comer {p} em {c}º lugar.")

# Tupla 2.0
num = (1, 2, 5, 7, 3, 4, 6)
print(sorted(num))

# Tupla 2.1
a = (1, 2, 5, 7)
b = (3, 4, 6)
c = a + b
print(c)

# Tupla 2.2
a = (1, 2, 5, 7)
b = (3, 4, 6)
c = a + b
print(f"n[a U b] = {len(c)}")

# Tupla 2.3
a = (1, 2, 5, 7)
b = (3, 4, 6)
c = a + b
print(c.index(6))

