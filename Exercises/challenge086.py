def lin():
    print("-=" * 12)


lin()
print(" == MATRIZ EM PYTHON == ")
lin()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para a coordenada [{l}, {c}] "))

lin()
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^3}]", end=" ")
    print()
lin()

