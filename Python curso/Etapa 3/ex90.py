from os import system
system('cls')

aluno = {}

aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('='*30 + f'\n{" BOLETIM ":^30}\n' + '='*30)
for chave, valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')