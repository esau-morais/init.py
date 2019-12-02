# Crie as duas variáveis B e T:
B = int(input())
T = int(input())
nota = (160 * 70)
areabt = int(B + T) * (70 / 2)
# F == Esquerda
# M == Direita
# Condições para validar:
if areabt > nota / 2:
    print(1)
elif areabt == nota / 2:
    print(0)
elif areabt < nota / 2:
    print(2)
