from os import system
from datetime import date
import time
system('cls')

'''for i in range(1, 10):
    if '.' == '.':
        for i in range(1):
            time.sleep(1)
            print('Segredo!')
    system('cls')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('..')
    time.sleep(1)
    print('...')
    time.sleep(1)'''
    
'''for i in range(0, 7): #Conta de 0 até 7
    print(i)
print('FIM')'''

'''for i in range(7, 0, 4):  # for i in range(Começo: FiM: Passos)
    print(i)
print('FIM')'''

'''Num = int(input('Início: '))
Fim = int(input('Fim: '))
Pass = int(input('Passo:'))
for i in range(Num, Fim+1, Pass):
    print(i)'''
    
'''s = 0
for i in range(0, 4):
    n = int(input('Digite um número: '))
    s += n
system('cls')
print(f'Soma dos valores foi {s}.')'''

# Exercicio 1 / 10 até 0 com uma pausa 1 pausa de segundo entre cada número
'''for i in range(10 , 0, -1):
    print(i)
    time.sleep(1)'''
    
# Exercicio 2 / Mostrar somentes pares de 1 até 50.
'''for i in range(1 , 51, 2):
    print(i, end=' ')
print('\nFim verificação!')'''

# Exercicio 3 / Armazenar números impares   
'''soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        soma += i
print(f'A soma dos {cont} ímpares múltiplos de três é: {soma}')'''

# Exercicio 4 / Tabuada
'''tab = int(input('Digite número para tabuada: '))
for i in range(1, 11):
    print(f'{tab} x {i} = {i * tab}')'''
    
# Exercicio 5 / Calcular pares somente de 6 números 
'''par = 0
cont = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i} valor: '))
    if num % 2 == 0:
        par += num
        cont += 1
print(f'Soma dos números pares {cont} e soma sendo {par}.')'''

# Exercicio 6 / Primeiro termo e razão de uma PA mostrar 10 primeiros termos]
'''primeiro_termo = int(input('Digite termo da PA: '))
razao = int(input('Digite as razão da PA: '))

for i in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
    print(i, end='-> ')
    
print('Fim!')'''

# Exercicio 7 /  Ler se um número e primo ou não
'''num = int(input('\033[3;34mVerificador número primo --> \033[m'))
print('\033[36m-=-\033[m' *10)
print('')
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print('{} '.format(i), end='')
print('\n')
print('\033[36m-=-\033[m' *10)
if tot == 2:
    print(f'\033[m\033[3;32mO número -> {num} é primo, e foi divisível {tot} vezes.')
else:
    print(f'\033[m\033[1;31mNúmero {num} não é primo!, e foi divisivel {tot} vezes.')
print('\033[m')'''

# Exercicio 8 / Leia uma str e verifica se é um palindromo
'''frase = input("Digite uma frase para verificar se é um palíndromo: ")
frase_sem_espacos = frase.replace(" ", "").lower()
if frase_sem_espacos == frase_sem_espacos[::-1]:
    print(f"\033[32mA frase \033[3;33m{frase}\033[m\033[32m, é um palíndromo!\033[m")   
else:
    print(f"\033[3;35mA frase \033[1;31m{frase}\033[m\033[3;35m, não é um palíndromo.\033[m")'''
    
# Exercicio 9 / Ler ano nascimento e dizer quantos já são maiores idade
'''totM = 0
totN = 0
for i in range(1, 7):
    ano = int(input(f'{i} |Digite ano nascimento: '))
    idade = abs(ano - date.today().year)
    if idade >= 21:
        totM += 1
    elif idade < 21:
        totN += 1
print(f'Existe {totM} pessoa(s) maior(es) idade é {totN} menor(es) idade.')'''

# Exercicio 10 / Ler pesso de 5 pessoas mostrar qual foi maior qual foi menor
'''tot = []
for i in range(1, 6):
    pesso = float(input(f'{i} | Qual seu pesso: '))
    tot.append(pesso)
print(f'O maior pesso e {max(tot):.2f} Kg é menor sendo {min(tot):.2f} Kg.')'''

# Exercicio 11 / Ler nome, idade e sexo dizer media idade,qual homen mais velho e qualtas mulheres tem menos 20 anos
idades = []
totM = 0
nomeM = ''
idadeM = 0
for i in range(1, 5):
    print(f'===== {i} Pessoa =====')
    nome = input(f'Nome: ')
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo M/F: ')
    idades.append(idade)
    if sexo in 'Mm' and idade > idadeM:
        nomeM = nome
        idadeM = idade
    if sexo in 'Ff' and idade < 20:
        totM += 1
media = sum(idades) / len(idades)
print(f'Média idade do grupo é de {media:.2f}')
print(f'O homem mais velho é {nomeM} com {idadeM} anos.')
print(f'Temos um total de {totM} mulheres com menos de 20 anos.')