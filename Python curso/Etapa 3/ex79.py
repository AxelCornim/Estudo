from os import system
system('cls')

numeros = []

while True:
    N1= int(input('Digite um valor: '))
    if N1 not in numeros:
        numeros.append(N1)
        print('Processando...\nValor Adicionado.')
    else:
        print('Valor Duplicado! Valor inválido!')
    resposta = ''   
    r = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if r in 'N':
        break
print('-=-'*15)
print(f'Você Digitou os valores {sorted(numeros)}')