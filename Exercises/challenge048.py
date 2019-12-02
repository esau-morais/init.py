soma = 0
for c in range(1,501,2):
   if c%3 == 0:
        soma = soma + c
print("O somatório de todos os números inteiros ímpares, divisíveis por 3, entre 1 e 501 é: {}".format(soma))