import random
num = int(random.randint(0,5))
u = int(input("Tente descobrir qual o número escolhido:"))
if u==num:
    print("Parabéns! Você venceu!")
else:
    print("Que pena! Você perdeu!")
print("O número escolhido foi {}".format(num))