# Com limite
c = 1
while c < 11:
    print(c)
    c += 1

# Sem limite
num = 1
while num != 0:
    num = int(input("Digite um número inteiro: "))

# Limite determinado pelo usuário
num = 1
resp = "S"
while resp == "S":
    num = int(input("Digite um número inteiro: "))
    resp = str(input("Deseja continuar? [S/N]")).upper()

# Quant. de números pares e ímpares
num = 1
par = impar = 0
while num != 0:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print("A quantidade de números pares é {} e de ímpares é {}".format(par,impar))