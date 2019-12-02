import math
cat1=float(input("Digite um valor para o cateto oposto:"))
cat2=float(input("Digite um valor para o cateto adjacente:"))
hyp= math.hypot(cat1,cat2)
print("A hipotenusa do triângulo retângulo, de catetos {} e {}, é: {}".format(cat1,cat2,hyp))