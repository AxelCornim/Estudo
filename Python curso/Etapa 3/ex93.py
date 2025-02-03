from os import system
system('cls')

jogador = {}

jogador['Nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

gols = []

for partida in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {partida+1}? ')))

jogador['Gols'] = gols
jogador['Total de Gols'] = sum(gols)

print('='*30)
print(f'{" APROVEITAMENTO DO JOGADOR ":^30}')
print('='*30)

for indice, (chave, valor) in enumerate(jogador.items()):
    print(f'{indice+1}. {chave}: {valor}')
print('='*30)
for chave, valor in jogador.items():
    print(f'{chave}: {valor}')
print('='*30)
print(f'Foram registradas {len(jogador["Gols"])} partidas.')
print('='*30)
print(f'O jogador fez um total de {jogador["Total de Gols"]} gols.')

print('='*30)