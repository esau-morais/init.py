#Tempo de algo: condição composta
tempo = int(input("Digite quantos anos tem seu veículo:"))
if tempo<=3:
    print("Seu veículo é novo!")
else:
    print("Seu veículo é velho!")
print("--Fim!--")

#Tempo de algo: condição simplificada
tempo = int(input("Digite quantos anos tem seu veículo:"))
print("Seu veículo é novo!" if tempo<=3 else "Seu veículo é velho!")
print("--Fim!--")

#Nome: Condição simples
nome = str(input("Digite seu nome:"))
if nome == "Esaú":
    print("Que nome diferente!")
print("Prazer em conhecê-lo, {}!".format(nome))

#Nome: Condição composta
nome = str(input("Digite seu nome:"))
if nome == "Esaú":
    print("Que nome diferente!")
else:
    print("Que nome normal!")
print("Prazer em conhecê-lo, {}!".format(nome))

#Notas: Condição composta
n1 = float(input("Digite a nota do aluno:"))
if n1>6:
    print("Parabéns! Você foi aprovado!")
else:
    print("Você ficou de recuperação")

#Média: Condição composta
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))
m = (n1 + n2) / 2
print("A sua média foi {}".format(m))
if m>6:
    print("Você está aprovado!")
else:
    print("Você está reprovado")