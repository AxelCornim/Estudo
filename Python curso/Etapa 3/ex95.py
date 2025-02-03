from os import system
system('cls')

jogadores = []

while True:
    jogador = {}

    jogador['Nome'] = input('Digite o nome do jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    gols = []
    total_gols = 0
    for partida in range(1, partidas+1):
        gol = int(input(f'Quantos gols na partida {partida}? '))
        gols.append(gol)
        total_gols += gol

    jogador['Gols'] = gols
    jogador['Total Gols'] = total_gols

    jogadores.append(jogador)

    continuar = input('Deseja cadastrar outro jogador? (S/N): ').upper()
    if continuar != 'S':
        break

print('='*40 + f'\n{" APROVEITAMENTO ":^40}\n' + '='*40)

for jogador in jogadores:
    print(f'Nome: {jogador["Nome"]}')
    print(f'Gols: {jogador["Gols"]}')
    print(f'Total de Gols: {jogador["Total Gols"]}')
    print('-'*40)