import random
from os import system
system('cls')

jogadores = {}

for i in range(1, 5):
    resultado = random.randint(1, 6)
    jogadores[f'Jogador {i}'] = resultado

print('='*30 + f'\n{" RESULTADOS DOS DADOS ":^30}\n' + '='*30)

for jogador, resultado in jogadores.items():
    print(f'{jogador}: {resultado}')

print('='*30)
print(f'{" RANKING ":^30}')
print('='*30)

ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

for i, (jogador, resultado) in enumerate(ranking, start=1):
    print(f'{i}º lugar: {jogador} com {resultado} pontos')



