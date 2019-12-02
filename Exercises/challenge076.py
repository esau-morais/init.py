def lin():
    print("-=" * 13)


lin()
print(" == LISTAGEM DE PREÇOS == ")
lin()

notebook = ("Jumper Ezbook 3 Pro", "R$1470,00".strip())
capa = ("Capa para Notebook", "R$200,00".strip())
mouse = ("Mouse Wireless", "R$45,00".strip())
fone = ("Fone de Ouvido Wireless", "R$114,00".strip())
celular = ("Smartphone Xiaomi Mi 8 Plus", "2400,00".strip())

for c in notebook, capa, mouse, fone, celular:
    print(c[0], end=":\n")
    print(c[1], end="\n")
