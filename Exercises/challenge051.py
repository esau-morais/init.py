num = int(input("Digite o primeiro termo: "))
pa = int(input("Digite a razão: "))
dec = num + (10 - 1) * pa
for c in range(num,dec,pa):
    print("{}".format(c), end="→")
print("FIM")