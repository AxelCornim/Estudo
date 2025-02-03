from os import system
system('cls')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior_valor = matriz[0][2]
sum_terceira_coluna = 0
soma_par = 0

for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para [{i}][{j}]: "))

for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]', end=' ')
    print()

for i in range(3):
    for j in range(3):
        if matriz[i][j] % 2 == 0:
            soma_par += matriz[i][j]

for i in range(3):
    sum_terceira_coluna += matriz[i][2]

for i in range(1, 3):  # Começando a partir da segunda linha
    if matriz[i][2] > maior_valor:
        maior_valor = matriz[i][2]

print(f'A soma dos valores pares é: {soma_par}.')
print(f'A soma dos valores da terceira coluna é {sum_terceira_coluna}.')
print(f'O maior valor da terceira coluna é {maior_valor}.')