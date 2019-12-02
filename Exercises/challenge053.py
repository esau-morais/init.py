frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = ""
for letra in range(len(juntas) -1,-1,-1):
    inverso += juntas[letra]
print("O inverso de {} é {}".format(frase,inverso))
if inverso == juntas:
    print("A frase digitada é um \033[33mPalíndromo\033[m.")
else:
    print("A frase {} \033[31mnão é\033[m um \033[33mPalíndromo\033[m.".format(frase))