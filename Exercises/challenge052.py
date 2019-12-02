num = int(input("Digite um número inteiro: "))
total = 0
for c in range(1,num + 1):
    if num % c == 0:
        total += 1
        print("\033[33m", end=" ")
    else:
        print("\033[31m", end=" ")
    print("{}".format(c), end=" ")
print("\n\033[mO número {} foi divisível por {} números.".format(num,total))
if total == 2:
    print("O número {} \033[33mé primo\033[m.".format(num))
else:
    print("O número {} \033[31mnão é primo\033[m.".format(num))