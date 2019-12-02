from datetime import date
atual = date.today().year
maior = 0
menor = 0
for p in range(1,8):
    ano = int(input("Digite o ano em que a {}ª pessoa nasceu: ".format(p)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print("{} pessoa(s) \033[33matingiram\033[m a \033[33mmaioridade\033[m".format(maior))
print("{} pessoa(s) \033[31mnão atingiram\033[m a \033[33mmaioridade\033[m.".format(menor))
