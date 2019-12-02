import time
def lin():
    print("-=" * 13)


lin()
print(" == NÚMEROS EM EXTENSO == ")
lin()

nums = ('zero', 'um', 'dois', 'três',
 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 
 'dez', 'onze', 'doze', 'treze', 'catorze', 
  'quinze', 'dezesseis', 'dezessete', 'dezoito', 
  'dezenove', 'vinte')
while True:
    num = int(input("Digite um número inteiro entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    else:
        pass
print(f"Você digitou o número {nums[num]}")
time.sleep(1.0)
print("Finalizando")
time.sleep(0.5)
print("O")
time.sleep(0.5)
print("Programa")
time.sleep(0.5)
print("...")
time.sleep(1.0)
print("Programa finalizado com sucesso. Volte sempre!")
