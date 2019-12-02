def lin():
    print("-=" * 20)


lin()
print(" == ANÁLISE DE EXPRESSÕES MATEMÁTICAS == ")
lin()

exp = str(input("Digite uma expressão matemática: "))
exps = []
for simb in exp:
    if simb == "(":
        exps.append("(")
    elif simb == ")":
        if len(exps) > 0:
            exps.pop()
        else:
            exps.append(")")
            break
if len(exps) == 0:
    print("Expressão matemática validada!")
else:
    print("Expressão matemática inválida.")
