from os import system
system('cls')

# Inicializa a lista vazia
numeros = []

# Loop para a entrada de números
while True:
    num = int(input('Digite um número: '))
    user =  str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    numeros.append(num)
    if user in 'N':
        break

# A) Quantos números foram digitados
quantidade = len(numeros)

# B) Lista ordenada de forma decrescente
numeros.sort(reverse=True)

# C) Verifica se o valor 5 está na lista
tem_cinco = 5 in numeros

# Mostra os resultados
print('-=-'*10)
print(f'Foram digitados {quantidade} números.')
print(f'Lista em ordem decrescente: {numeros}')
print(f'O valor 5 {"está" if tem_cinco else "não está"} na lista.')
