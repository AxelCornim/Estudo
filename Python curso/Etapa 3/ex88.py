from random import sample
from time import sleep
from os import system
system('cls')

# Gera cabeçalho
print(f'-'*30 + f'\n{"JOGO DO MEGA DEV":^30}\n' + '-'*30)

# Pergunta quantos jogos serão gerados
quantidade_jogos = int(input('Quantos jogos deseja sortear? '))

# Adereço de texto
print(f'-=-=-= SORTEANDO {quantidade_jogos} GAMEX =-=-=-')

# Gera os palpites
palpites = []
for _ in range(quantidade_jogos):
    palpite = sample(range(1, 61), 6)
    palpites.append(palpite)

# Exibe os palpites gerados
for i, palpite in enumerate(palpites, 1):
    print(f'Jogo {i}: {sorted(palpite)}')
    sleep(1)

# Mensagem final
print('-=-=-=-=- < GOOD LUCK! > -=-=-=')