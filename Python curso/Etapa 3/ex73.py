from os import system
system('cls')

times_brasileirao = (
    'Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
    'Palmeiras', 'Santos', 'Grêmio', 'Athletico-PR', 'Corinthians',
    'Bragantino', 'Chapecoense', 'Atlético-GO', 'Sport Recife', 'Bahia', 'Fortaleza',
    'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo'
)

print('='*30)
print(f'Os 5 primeiros times são: {times_brasileirao[:5]}')
print('='*30)
print(f'Os últimos 4 colocados são: {times_brasileirao[-4:]}')
print('='*30)
print(f'Times em ordem alfabética: {sorted(times_brasileirao)}')
print('='*30)
print(f'A Chapecoense está na {times_brasileirao.index("Chapecoense")+1}ª posição.')