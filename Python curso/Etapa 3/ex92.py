from datetime import datetime
from os import system
system('cls')

dados = {}

dados['Nome'] = input('Digite o nome: ')
ano_nascimento = int(input('Digite o ano de nascimento: '))
dados['Idade'] = datetime.now().year - ano_nascimento
dados['CTPS'] = int(input('Digite o número da CTPS (0 se não tiver): '))

if dados['CTPS'] != 0:
    dados['Ano Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o salário: '))
    dados['Aposentadoria'] = dados['Ano Contratação'] + 35 - ano_nascimento

print('='*30 + f'\n{" DADOS CADASTRADOS ":^30}\n' + '='*30)

for chave, valor in dados.items():
    print(f'{chave}: {valor}')

print('='*30)