import time

def lin():
    print("-=" * 12)


lin()
print(" == BOLETIM ESCOLAR == ")
lin()

lista = list()

while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break

lin()
print(f'{"Nº":<8}{"Nome":<8}{"Média":>6}')
lin()

for i, a in enumerate(lista):
    print(f'{i:<8}{a[0]:<8}{a[2]:>6.1f}')

while True:
    opc = int(input('Deseja mostrar a nota de qual aluno? '))
    if opc == 999:
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
time.sleep(0.5)
print("FINALIZANDO ")
time.sleep(0.5)
print("O ")
time.sleep(0.5)
print("PROGRAMA ")
time.sleep(1.5)
print(" == VOLTE SEMPRE! ==")
