def lin():
    print("-=" * 12)


lin()
print(" == MATRIX ON PYTHON == ")
lin()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sump = major = sumc = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Enter a value for the coordinate [{l}, {c}]: "))

lin()
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^3}]", end=" ")
        if matriz[l][c] % 2 == 0:
            sump += matriz[l][c]
    print()
lin()
print(f"The sum of the paired values entered is: {sump}")

for l in range(0,3):
    sumc += matriz[l][2]
print(f"The sum of the values in the 3rd column is: {sumc}")

for c in range(0,3):
    if c == 0:
        major = matriz[1][c]
    elif matriz[1][c] > major:
        major = matriz[1][c]
print(f"The highest value entered in the 2nd row is: {major}")
