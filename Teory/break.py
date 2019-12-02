# Interrompendo uma variável
num = 0
while True:
    num = int(input("Digite um número inteiro: "))
    if num == 10:
        break

# Interrompendo mais de uma variável
n = soma = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 10:
        break
    soma += n
print(f"A soma dos valores é: {soma}")