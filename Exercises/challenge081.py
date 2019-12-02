def lin():
    print("-=" * 14)



lin()
print(" == DADOS PARA UMA LISTA == ")
lin()

dados = []

while True:
    dados.append(int(input("Digite um número: ")))
    resp = str(input("Deseja continuar? [S/N] "))
    if resp in "Nn":
        break

print(f"Você digitou {len(dados)} número(s).")
dados.sort(reverse=True)
print(f"O(s) número(s), em ordem decrescente, fica(m): {dados}.")

if 5 in dados:
    print("O número 5 foi encontrado na lista!")
else:
    print("O número 5 não foi encontrado na lista.")
