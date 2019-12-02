import random,time
def lin():
    print("-=" * 13)


lin()
print(" == SORTEIO DE NÚMEROS == ")
lin()

nsort = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))

time.sleep(1.0)
print("Os números sorteados foram: ", end=" ")
for c in nsort:
    print(f"{c}", end=" ")
print(f"\nO maior número sorteado foi: {max(nsort)}")
print(f"O menor número sorteado foi: {min(nsort)}")
time.sleep(1.0)
print("Finalizando")
time.sleep(1.0)
print("O")
time.sleep(1.0)
print("Programa")
time.sleep(1.0)
print("...")
time.sleep(1.0)
print("Programa finalizado com sucesso. Volte sempre!")
