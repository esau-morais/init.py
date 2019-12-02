v = float(input('Digite a velocidade do carro:'))
if v>80:
    print("Você foi multado")
m = 7 * (v - 80)
print("A sua multa foi de {} reais".format(m))