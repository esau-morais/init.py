import time
def lin():
    print("-=" * 12)


lin()
print(" == ANÁLISE DE DADOS == ")
lin()

num = (int(input("Digite um número: ")),
int(input("Digite outro número: ")),
int(input("Digite mais um número: ")),
int(input("Digite o último número: ")))

valores = (num)
print(f"Os valores digitados foram: {valores}")

num9 = valores.count(9)
print(f"O número 9 apareceu {num9} vez(es)")

if 3 in num:
    print(f"O número 3 está na {num.index(3)+1}ª posição")
else:
    print("O número 3 não foi digitado em nenhuma posição.")

print(f"O(s) número(s) par(es) digitado(s) foi(ram): ",end=" ")
for n in num:
    if n % 2 == 0:
        print(n)
time.sleep(1.0)
print("Finalizando")
time.sleep(1.0)
print("O")
time.sleep(1.0)
print("Programa")
time.sleep(1.0)
print("...")
time.sleep(1.3)
print("Programa finalizado com sucesso. Volte sempre!")
