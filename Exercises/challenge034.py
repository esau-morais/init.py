sal = float(input("Digite o seu salário:"))
sal1 = float(sal + (1250/10))
sal2 = float(sal + (sal*0.15))
if sal>1250:
    print("O seu novo salário será: {}".format(sal1))
else:
    print("O seu novo salário será: {}".format(sal2))