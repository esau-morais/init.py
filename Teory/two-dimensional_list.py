num = int(input())
lista = [[0] * num for i in range(num)]
for i in range(num):
    for j in range(num):
        if i < j:
            lista[i][j] = 0
        elif i > j:
            lista[i][j] = 2
        else:
            lista[i][j] = 1
for r in lista:
    print(' '.join([str(elem) for elem in r]))
