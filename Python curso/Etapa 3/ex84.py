from os import system
system('cls')

# Inicializa as listas
pessoas = []
mais_pesadas = []
mais_leves = []

# Loop para cada pessoa
while True:
    # Obtém nome e peso
    nome = input('Nome: ')
    peso = float(input('Pesso: '))

    # Adiciona à lista de pessoas
    pessoas.append((nome, peso))

    # Pergunta se deseja continuar
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

# A) Quantas pessoas foram cadastradas.
total_pessoas = len(pessoas)

# B) Encontra as pessoas mais pesadas
peso_maximo = max(pessoas, key=lambda x: x[1])[1]
mais_pesadas = [pessoa for pessoa in pessoas if pessoa[1] == peso_maximo]

# C) Encontra as pessoas mais leves
peso_minimo = min(pessoas, key=lambda x: x[1])[1]
mais_leves = [pessoa for pessoa in pessoas if pessoa[1] == peso_minimo]

# Exibe os resultados
print('='*30)
print(f'Foram cadastradas {total_pessoas} pessoas.')
print(f'O maior peso foi de {peso_maximo}. Peso de ', end='')
for pessoa in mais_pesadas:
    print(f'{pessoa[0]}', end=' ')
print(f'\nO menor peso foi de {peso_minimo}. Peso de ', end='')
for pessoa in mais_leves:
    print(f'{pessoa[0]}', end=' ')
