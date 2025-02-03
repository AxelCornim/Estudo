from os import system
system('cls')

# Lista composta para armazenar os dados dos alunos
alunos = []

# Loop para inserir dados dos alunos
while True:
    nome = input('Digite o nome do aluno: ')

    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))

    # Adiciona os dados do aluno à lista de alunos
    alunos.append([nome, [nota1, nota2]])

    request = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if request == 'N':
        break

# Exibe boletim com média
print('='*30 + f'{"BOLETIM":^30}' + '='*30)
print(f'{"Nº":<4}{"NOME":<15}{"MÉDIA":>10}')
print('-'*30)

for i, aluno in enumerate(alunos, start=1):
    nome = aluno[0]
    notas = aluno[1]
    media = sum(notas) / len(notas)
    print(f'{i:<4}{nome:<15}{media:>10.2f}')

# Permite que o usuário veja as notas de um aluno específico
while True:
    print('='*30)
    escolha = input('Deseja ver as notas de algum aluno? (s/n): ')
    if escolha.lower().strip() != 's':
        break
    print('='*30)
    aluno_escolhido = input('Digite o nome do aluno: ')
    for aluno in alunos:
        if aluno[0] == aluno_escolhido:
            notas = aluno[1]
            print('='*30)
            print(f'Notas de {aluno[0]}: {notas[0]} e {notas[1]}')
            print('='*30)
            break
    else:
        print(f'Aluno "{aluno_escolhido}" não encontrado.')
print('<<< ACABOU !!! >>>')