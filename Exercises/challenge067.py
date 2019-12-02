def lin():
    print("-=" * 21)


num = 0
lin()
num = int(input("Digite um número para ver sua tabuada: "))
lin()

for c in range(1,11):
        print(f"{num} x {c} = {num * c}")

while True:
    lin()
    num = int(input("Digite um número para ver sua tabuada: "))
    if num < 0:
        break
    for c in range(1,11):
        print(f"{num} x {c} = {num * c}")
