from os import system
system('cls')

# Inicialize a matriz como uma lista de listas
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preencha a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f'Digite o valor para [{i}][{j}]: '))

# Mostre a matriz formatada
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()