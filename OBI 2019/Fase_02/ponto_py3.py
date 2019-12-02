P = int(input()) # Passos
if P < 1 or P > 50: 
    exit()
print(int(((4 ** P)** (0.5) + 1) ** 2)) # Pontos
