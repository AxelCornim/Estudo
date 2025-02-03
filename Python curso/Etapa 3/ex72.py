from os import system
system('cls')
    
numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
                   'cinco', 'seis', 'sete', 'oito', 'nove', 
                   'dez', 'onze', 'doze', 'treze', 'catorze', 
                   'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número {num} por extenso é {numeros_extenso[num]}.')
        continuar = input('Deseja continuar ? [S/N]').strip().upper()
        if continuar == 'N':
            break
    else:
        print('Número inválido digite número entre [0/20].')