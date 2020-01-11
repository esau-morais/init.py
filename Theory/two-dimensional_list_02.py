# Primeira forma
bidimensional_list = [[2, 4, 6], [1, 3, 5], [7, 11, 13]] # Lista bidimensional
for i in range(len(bidimensional_list)): # Loop para linhas 
    for j in range(len(bidimensional_list[i])): # Loop para as 'colunas'
        print(bidimensional_list[i][j], end=' ') # 'Print' de ambos
    print() # Espaço aplicado logo após cada lista
print('-=' * 4)
# Segunda forma
bidimensional_list_02 = [[2, 4, 6], [1, 3, 5], [7, 11, 13]]
for r in bidimensional_list_02:
    for e in r:
        print(e, end=' ')
    print()
print('-=' * 4)
# Terceira forma
bidimensional_list_02 = [[2, 4, 6], [1, 3, 5], [7, 11, 13]]
for r in bidimensional_list_02:
        print(' '.join([str(e) for e in r]))
print('-=' * 4)
# Soma dos termos
bidimensional_list_02 = [[2, 4, 6], [1, 3, 5], [7, 11, 13]]
s = 0
for r in bidimensional_list_02:
    for e in r:
        s += e
print(s)
