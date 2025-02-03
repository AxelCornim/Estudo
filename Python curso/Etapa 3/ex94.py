from os import system
system('cls')

# Lista que irá armazenar os dicionários de pessoas
pessoas = []

# Variáveis para calcular a média de idade
soma_idades = 0
total_pessoas = 0

# Listas para armazenar mulheres e pessoas acima da média
mulheres = []
acima_da_media = []

while True:
    pessoa = {}

    pessoa['Nome'] = input('Digite o nome da pessoa: ')
    pessoa['Sexo'] = input('Digite o sexo da pessoa (M/F): ').upper()
    pessoa['Idade'] = int(input('Digite a idade da pessoa: '))

    # Atualiza a soma das idades e o total de pessoas
    soma_idades += pessoa['Idade']
    total_pessoas += 1

    # Adiciona a pessoa à lista de pessoas
    pessoas.append(pessoa)

    # Verifica se a pessoa é mulher e a adiciona à lista de mulheres
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa)

    # Verifica se a pessoa tem idade acima da média e a adiciona à lista correspondente
    if pessoa['Idade'] > (soma_idades / total_pessoas):
        acima_da_media.append(pessoa)

    continuar = input('Deseja cadastrar outra pessoa? (S/N): ').upper()
    if continuar != 'S':
        break

# Calcula a média de idade
media_idade = soma_idades / total_pessoas

print('='*30)
# Mostra os resultados
print(f'Foram cadastradas {total_pessoas} pessoas.')
print(f'A média de idade é {media_idade:.2f} anos.')
print('Lista de mulheres:')
for mulher in mulheres:
    print(mulher)
print('Lista de pessoas acima da média de idade:')
for pessoa in acima_da_media:
    print(pessoa)