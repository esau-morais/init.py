import time
resp = "S"
soma =  total = med = 0

while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    total += 1
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
med = soma / total
print(f"Você digitou {total} números e a média dos valores foi {med}")
