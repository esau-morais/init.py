import time
def lin():
    print("-=" * 10)


lin()
print(" == Gerador de PA ==")
lin()

a1 = int(input("Digite o primeiro termo da sua PA: "))
r = int(input("Digite a razão da sua PA: "))
t = a1
cont = 1
total = 0
perg = 10
pa = a1 + (10 - 1) * r

while perg != 0:
    total += perg
    while cont <= total:
        print(f"{t} → ", end="")
        t += r
        cont += 1
    print("PAUSA")
    perg = int(input("Você deseja adicionar quantos termos à sua PA? "))
print("FIM")
time.sleep(1.0)
print("Finalizando")
time.sleep(1.0)
print("O")
time.sleep(1.0)
print("Programa")
time.sleep(1.0)
print("...")
time.sleep(1.0)
print(f"PA finalizada com {total} termos mostrados.")
