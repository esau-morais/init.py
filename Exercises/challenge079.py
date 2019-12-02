def lin():
    print("-=" * 13)


lin()
print(" == ANÁLISE DE VALORES == ")
lin()

nums = list()
while True:
    num = int(input("Digite um valor: "))
    if num not in nums:
        nums.append(num)
    else:
        print("Valor já digitado, portanto, não será adicionado.")
    perg = str(input("Deseja continuar? [S/N] "))
    if perg in "Nn":
        break
print("-=" * 23)
nums.sort()
print(f"Você digitou os seguintes valores: {nums}")
print("-=" * 23)
