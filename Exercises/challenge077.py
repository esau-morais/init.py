palavras = ("Segundo", "Computador", "Cadeira", "Celular", "Controle".strip())

for c in palavras:
    print(f"\nNa palavra {c} tem-se a(s) voagal(is) ", end="")
    for letra in c:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
