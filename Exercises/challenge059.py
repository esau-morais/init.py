import time
val1 = int(input("Digite um valor: "))
val2 = int(input("Digite outro valor: "))
dec = 0
while dec != 5:
    print('''    [1] SOMAR os dois valores
    [2] MULTIPLICAR os dois valores
    [3] Ver qual dos valores é MAIOR
    [4] Digitar NOVOS valores
    [5] SAIR do programa''')
    dec = int(input("O que você deseja fazer? "))
    if dec == 1:
        s = val1 + val2
        print(f"A soma entre os valores digitados é: {s}")
    elif dec == 2:
        m = val1 * val2
        print(f"A multiplicação entre os valores é: {m}")
    elif dec == 3:
        if val1 > val2:
            maior = val1
        else:
            maior = val2
        print(f"O maior dentre os valores é: {maior}")
    elif dec == 4:
        print("Informe os novos valores: ")
        val1 = int(input("Digite um novo valor: "))
        val2 = int(input("Digite outro valor: "))
    elif dec == 5:
        time.sleep(1.0)
        print("Finalizando")
        time.sleep(1.0)
        print("O")
        time.sleep(1.0)
        print("Programa")
        time.sleep(1.0)
    else:
        print("Valor inválido. Tente novamente")
    print("-=" * 18)
print("Fim do Programa. Volte sempre!")
