# introduzir com um título
def lin():
    print("-=" * 10)


lin()
print(" == PAR OU ÍMPAR? == ")
lin()

# fazer variáveis para os maiores e menores valores
maior = 0
menor = 0

# fazer variável para a lista
lista = []

for n in range(0,5):
    lista.append(int(input(f"Digite um número para a posição {n}: ")))
    if n == 0:
        maior = menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]
print(f"Os valores digitados foram: {lista}")
print(f"O maior número digitado foi: {maior}, na(s) posição(ções) ", end=" ")
for p, a in enumerate(lista):
    if a == maior:
        print(f"{p}. ", end=" ")
print()
print(f"O menor número digitado foi: {menor}, na(s) posição(ções) ", end=" ")
for p, a in enumerate(lista):
    if a == menor:
        print(f"{p}.. ", end=" ")
