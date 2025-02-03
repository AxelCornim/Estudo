from datetime import date
import random
import time
from os import system
system('cls')

# Exemplo de uso de "IF ELIF ELSE"
'''N1 = str(input('Qual seu nome? '))
if N1 == 'Luan':
    print('Nome bonito!')
elif N1 == 'Pedro' or N1 == 'Maria' or N1 == 'Paula':
    print('Seu nome é muito popular no Brasil.')  
elif N1 in 'Ana Maria':
    print('Que nome bonito moça!')
else:
    (print('Seu nome é normal.'))
print(f'Tenha um bom dia!{N1}.')'''

# Exercicio 1 Calcule o valor da prestação mensal. sabendo que ela não pode exceder 30% do salário ou então empréstimo séra negado.
'''casa = float(input('Qual valor casa deseja comprar? '))
compra = float(input('Qual seu salário? '))
QTP = float(input('Quantos anos deseja pagar? '))     # QTP = Quantidade total parcelas

parcela = casa / int(QTP*12)         # Divide valor casa pelo valor parcelas                
VPC = int(compra - (compra *0.70))          # Retira 70% deixando 30% do valor total 

if VPC >= parcela:                          # Caso parcela seja menor 30% séra aprovado
    print(f"\033[1;32mVocê pode pagar casa valor de {casa}! aproveite moradia com parcelas de {parcela:.2f}.\033[m")
elif VPC <= parcela:                        # Caso parcela seja maior que 30% séra renegado
    print(f"\033[4;31mVocê não pagar casa no valor de {casa} pois execede valor 30% em cada parcela que é {parcela:.2f}.\033[m")
print(f'Obrigação de pagar {parcela:.2f} reais e tendo mínimo possível pagar {VPC:.2f} reais.')'''
    
# Exercicio 2 /  Tabela Digite 1 para Transformar binário, digite 2 para transforma Octal e digite 3 para Hexadecimal
'''numberoot = int(input('Digite um número: '))
print('\033[33m-+-\033[m' *15)
number = int(input('Digite 1 para Binário \nDigite 2 para Octal \nDigite 3 para Hexadecimal \nDigite 4 para sair \nResponda: '))
print('\033[33m-+-\033[m' *15)
if number == 1:
    print(f'O número {numberoot} transformado em binário {bin(numberoot)[2:]}')
elif number == 2:
    print(f'O número {numberoot} transformado em octal {oct(numberoot)[2:]}.')
elif number == 3:
    print(f'O número {numberoot} transformado em hexadecimal {hex(numberoot)[2:]}.')
elif number == 4:
    print('....')
    time.sleep(1)
    print('....')
    time.sleep(1)
    print('Adeus')'''
    
# Exercicio 3 /  Primeiro maior valor e segundo e caso os dois seja iguais.
'''N1 = int(input('Digite primeiro valor: '))
N2 = int(input('Digite segundo valor: '))
if N1 > N2:
    print(f'\033[4;32mO primeiro número, {N1} é maior que segundo {N2}.\033[m')
elif N2 > N1:
    print(f'\033[3;33mO segundo número, {N2} é maior que primeiro {N1}.\033[m')
elif N1 == N1:
    print('')
    print(f'O primeiro e segundo números {N1} é {N2} são iguais.')
else:
    print('Erro 4:20')'''
    
# Exercicio 4 / Vai ler tempo que falta ou que passou de se alistar
'''ANO = int(input('Qual foi ano de seu nascimento: '))
alistaroot = abs(ANO - date.today().year)      # Calcula ano da pessoa -ano atual
alistar = abs(alistaroot - 18)                      # Pega diferança anos se alistar ou que passou
if alistaroot < 18:
    print(f'Ainda falta {alistar} anos para se alistar.')
    print(f'Você vai se alistar no ano {date.today().year + alistar}')
elif alistaroot == 18:  
    print('Você tem que se alistar agora!!!')
elif alistaroot > 18:
    print(f'Você se alistou {alistar} anos atrás.')
    print(f'Você se alistou no ano {date.today().year - alistar}')'''
    
# Exercicio 5 / Ler Nota 1 e Nota 2 e menos 5 reprovado 5 até 6.9 recuperação e média 7 ou superior aprovado
'''N1 = float(input('Qual sua primeira nota: '))
N2 = float(input('Qual sua segunda nota: '))
Nota = (N1+N2)/2
if Nota < 5:
    print('\033[4;31mVocê foi REPROVADO!\033[m')
elif Nota >= 5 and Nota <= 6.9:
    print('\033[32mVocê está em recuperação.\033[m')
elif Nota >= 7:
    print('\033[1;33mVocê foi APROVADO!!!\033[m')'''
    
# Exercicio 6 / 9 anos mirin, 14 anos infantil, 19 anos junior, 20 anos senior e acima 20 anos e master.
'''idaderoot = int(input('Qual e ano de seu nascimento: '))
idade = abs(idaderoot - date.today().year)
print('\033[31m-=+=-\033[m' *7)
print('Confederação Nacional de Natação')
print('\033[31m-=+=-\033[m' *7)
if idade > 6 and idade <= 9:
    print('Cla Mirim.')
elif idade <= 14:
    print('Você está na categoria infaltil.')
elif idade <= 19:
    print('Você está na categoria Junior.')
elif idade <= 25:                             # Exemplo anterior elif idade > 19 and idade <= 25: | Exemplo atual idade <= 25: verifica somente 19 < 25 pois ja verificou 14 > 19
    print('Você está na categoria Sênior.')
elif idade > 25:
    print('Você está na categoria Master.')'''
    
# Exercicio 7 / Nomear Equilátero, Isúsceles e um Escalena
'''lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    elif lado1 != lado2 != lado3 != lado1:
        print("É um triângulo escaleno.")
    else:
        print("É um triângulo isósceles.")
else:
    print("Não é possível formar um triângulo com esses lados.")'''
    
# Exercicio 8 /   Abaixo 18.5: Abaixo Peso | Entre 18.5 e 25: Peso ideal | 25 até 30:Sobrepeso | 30 até 40:Obesidade | Acima de 40:Obesidade
'''peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))
print('\033[32m-:-\033[m' *12)
IMC = peso/(altura ** 2)
if IMC <= 18.5:
    print(f'\033[33mVocê está abaixo do peso!, com IMC:\033[m {IMC:.1f}')
elif  18.5 <= IMC < 25:
    print(f'\033[34mO seu peso é ideal, com IMC:\033[m {IMC:.1f}')
elif 25 <= IMC < 30:
    print(f'\033[35mVocê está sobrepeso, com IMC:\033[m {IMC:.1f}')
elif 30 <= IMC < 40:
    print(f'\033[36mVocê está com obesidade, com IMC:\033[m {IMC:.1f}')
elif IMC >= 40:
    print(f'\033[1;31mVocê está com obesidade morbida!!!, com IMC:\033[m {IMC:.1f}')
print('\033[3;32mTenha uma vida saudável!\033[m')'''

# Exercicio 9 /  A vista:10% desconto | a vista cartão:5% desconto | em até 2x: Preço normal | 3x ou mais: No cartão 20% de juros
'''produto = float(input('Digite o preço da compra: '))
print('\033[33m-=-\033[m' *13)
print('')
tabela = int(input('Qual sua forma pagamento\nDigite 1 | A vista 10% desconto\nDigite 2 | A vista no cartão 5% desconto\nDigite 3 | 2x no cartão preço normal\nDigite 4 | 3x ou mais no cartão 20% de juros\nDigite resposta aqui: '))
if tabela == 1:
    print(f'A vista fica \033[4;31m{produto-(produto*0.10)} reais\033[m o produto.')
elif tabela == 2:
    print(f'A vista no cartão fica \033[1;31m{produto-(produto*0.05)} reais.\033[m')
elif tabela == 3:
    print(f'2x no cartão paga preço de \033[3;31m{produto} reais SEM JUROS.\033[m')
elif tabela == 4:
    parc = int(input('Qualtas parcelas deseja pagar? '))
    totparc = produto / parc
    print(f'Sua compra parcelada em {totparc:.2f} reais, vai ficar em \033[31m{produto+(produto*0.20)} reais.\033[m')
else: 
    print('\033[1;31mOPÇÂO INVÁLIDA!!!\033[m')
print('')
print('\033[33m-=-\033[m' *13)
print('Tenha um bom dia!')'''

# Exercicio 10 / Jogar Jokenpô com IA
'''user = str(input('Pedra, Papel ou Tesoura: '))
print('Jo')
time.sleep(1)
print('Ken')
time.sleep(1)
print('Po')
system('cls')
print('Jokenpo!')
opcoes = ['Pedra', 'Papel', 'Tesoura']
IA = random.choice(opcoes)
if IA == user:
    print('\033[33mVocê empatou!\033[m')
elif (
    (user == 'Pedra' and IA == 'Tesoura')
    or (user == 'Papel' and IA == 'Pedra')
    or (user == 'Tesoura' and IA == 'Papel')
):
    print(f'\033[1;32mVocê ganhou! Escolheu {user} e IA escolheu {IA}.\033[m')
else:
    print(f'\033[3;31mA IA ganhou! IA escolheu {IA} e você escolheu {user}.\033[m')'''