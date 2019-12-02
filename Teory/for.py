#Repetição 1
for s in range(0,5):
    print("Seja bem vindo ao Python!")

#Contagem
for s in range(0,6):
    print(s)

#Contagem inversa
for s in range(10,0,-1):
    print(s)
print("FIM!")

#Contagem alternada
for s in range(0,10,2):
    print(s)

#Ex com 1 var.
num = int(input("Digite um número: "))
for c in range(0,num + 1):
    print(c)

#Ex2 com + var.
i = int(input("Digite o início da sequência: "))
f = int(input("Digite o fim sequência: "))
a = int(input("Digite a alternância: "))
for c in range(i,f + 1,a):
    print(c)

#Repetição 2
for c in range(0,10):
    nome = str(input("Digite o seu nome: "))

#Repetição 3
for c in range(0,10):
    num = int(input("Digite um número inteiro: "))

#Repetição + val: Ex 1
s = 0
for c in range(0,10):
    num = int(input("Digite um número inteiro: "))
    s += num
print("O somatório de todos os números inteiros é: {}".format(s))
