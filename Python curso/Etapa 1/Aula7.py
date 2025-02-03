from os import system
system("cls")

#print(5+2)
#print(5-2)
#print(5*2)
#print(5/2)
#print(5**2)
#print(5//2)
#print(5%2 )

#print('='*50)

#Name = input('Qual seu nome? ')
#print(f'Olá {Name:=^20}!')
#print('Olá {:>20}!'.format(Name))

#N1 = int(input('Primeiro valor: '))
#N2 = int(input('Segundo valor: '))
#S = N1 + N2
#M = N1 * N2
#D = N1 / N2
#DI = N1 // N2
#E = N1 ** N2

#print(f'A soma é {S}, o produto é {M} e a divisão é {D:.2f}', end=' | ')
#print(f'A divisão inteira {DI} e potência {E}')

#Exercicio 1       sucessor e antecessor
N1 = int(input('Digite um número: '))
print(f'Número atual sendo \033[1m\033[7;36;40m{N1}\033[m\033[m seu antecessor \033[36m{N1-1}\033[m é seu sucessor \033[36m{N1+1}\033[m.')

#Exercicio 2       dobro e triplo sua raiz quadrada
N1 = int(input('Digite um número: '))
print(f'O dobro de \033[7;33m{N1}\033[m e \033[4;33m{N1*2}\033[m e triplo \033[4;33m{N1*3}\033[m, tendo sua raiz quadrada \033[1;33m{N1**(1/2):.2f}\033[m.')

#Exercicio 3       Média de N1 e N2
N1 = float(input('Primeira nota: '))
N2 = float(input('Segunda nota: '))
print(f'Sua nota foi de \033[1;34m{(N1+N2)/2}\033[m')

#Exercicio 4      Metros para cm, cm para mm
N1 = float(input('Digite km deseja converter: '))
print(f'\033[35m{N1:.0f}\033[m Km equivale a Metros equivale a \033[4;35m{N1*100000:.0f}\033[mcm é tambem a \033[4;35m{N1*1000000:.0f}\033[mmm.')

#Exercicio 5       Tabuada
N1 = int(input('Digite número para calculada: '))
#print('{} x {} = {}'.format(N1, 1, N1*1))
print('-' * 12)
print(f'{N1} x 1 = \033[1;32m{N1*1}\033[m\n{N1} x 2 = \033[1;32m{N1*2}\033[m\n{N1} x 3 = \033[1;32m{N1*3}\033[m\n{N1} x 4 = \033[1;32m{N1*4}\033[m\n{N1} x 5 = \033[1;32m{N1*5}\033[m\n{N1} x 6 = \033[1;32m{N1*6}\033[m\n{N1} x 7 = \033[1;32m{N1*7}\033[m\n{N1} x 8 = \033[1;32m{N1*8}\033[m\n{N1} x 9 = \033[1;32m{N1*9}\033[m\n{N1} x 10 = \033[1;32m{N1*10}\033[m')
print('-' * 12)

#Exercicio 6      Converter Real para Dolar
N1 = float(input('Qualto deseja converter para dolares: '))
print(f'Você tem em US $\033[1;36m{N1/3.27:.2f}\033[m')

#Exercicio 7        Tinta nessesaria para pintar uma parede
N1 = float(input('Altura da parede: '))
N2 = float(input('Largura da parede: '))
print(f'Para pintar essa parede e necessário \033[34m{(N1*N2)/2}\033[m litros de tinta.')

#Exercicio 8        5% Desconto
N1 = float(input('Digite preço produto: '))
print(f'O produto que custava R$\033[7;36m{N1:.2f}\033[m Reais com 5% de desconto fica R$\033[1m\033[7;36m{N1-(N1*0.05):.2f}\033[m\033[m Reais.')

#Exercicio 9        15% Adicional
N1 = float(input('Qual valor do seu sálario: '))
print(f'O seu sálario de R$\033[35m{N1:.2f}\033[m Reais com aumento 15% fica em R$\933[1m\033[7;35m{N1+(N1*0.15):.2f}\033[m\033[m Reais.')