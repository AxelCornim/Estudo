from datetime import date
import random
import time
import math
from os import system
system("Cls")

'''if carro.esquerda():
    bloco True
else:
    bloco False'''
    
    # Primeira forma
'''temp = int(input("Qualtos anos tem seus carro? "))
if temp<= 3:
    print("Carro novo")
else:
    print("Carro velho")
print("--FIM--")'''

    # Condição simplificada
'''tempo = int(input("Qualtos anos tem seu caro? "))
print("Carro novo" if tempo<=3 else "Carro velho")
print("--FIM--")'''

# Exercicios em aula
'''nome = str(input("Qual seu nome? "))
if nome == "Gustavo":
    print("Que nome elegante você tem!")
print(f"Bom dia, {nome}!")'''

# 2
'''N1 = float(input("Qual a sua primeira nota: "))
N2 = float(input("Qual a sua segunda nota: "))
S = (N1+N2)/2
print(f"A sua média foi {S:.1f}")'''
# Forma simplificada
'''print("Parabéns"if S >= 6 else "STUDY!!!")'''
# Forma longa
'''if S >= 6.0:
    print("Sua médias foi boa! NICE!")
else:
    print("Sua média foi ruim! STUDY!!!")'''
    
# Exercicio 1     Acetar um número que foi escolhido aleatório de 0 a 5
'''NA = random.randint(0, 5)     # Gera número aleatorio 0 a 5   # NA = Number Random 
AN = int(input("Adivinhe um número entre 0 e 5: ")) # AN = Adivinhação número
if AN == NA:
    print("Você acertou")
else:
    print(f"Você errou número era {NA}")'''
# Exercicio 1 v2
machine = random.randint(0, 5)
print('\033[34m-=-\033[m' *20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('\033[34m-=-\033[m' *20)
player = int(input('Em que número eu pensei? '))
print("Carregando...")
time.sleep(2)
if player == machine:
    print('\033[1;30;47mParabéns você acertou!\033[m')
else:
    print(f"Maquina ganhou, você pensou \033[33m{player}\033[m sendo era \033[4;33m{machine}\033[m")
    
# Exercicio 2     Leia Km/h que um carro andava, caso pase 80km/h Receber mensagem multa é tambem cada km/h acima limite séra pagado R$7.00 por cada km
VM = float(input("Qual velocidade você estava dirigindo? ")) # VM = Velocidade do motorista
if VM > 80:
    print(f"Você ultrapassou Km/h permitido na via, pagara uma multa de R$\033[1;31m{(VM-80)*7:.2f}\033[m reais.")
print("Coduza com responsabilidade!")

# Exercicio 3   ler se e impar ou par
print("Verificador de impar ou par")
IOP = float(input("Digite um número: "))  # IOP = Impar ou Par
if IOP % 2 == 0:
    print(f"O número \033[36;47m{IOP:.0f}\033[m é par.")
else:
    print(f"O número \033[7;36;47m{IOP:.0f}\033[m é impar.")
    
# Exercicio 4    R$0,50 = 200km rodados tendo viagem mais longas sendo cobrado R$0.45
'''print("Catraca virtual / Valor por Km, R$0.50 por 200 KM é R$0.45 para viagens acima 200km")
PAG = float(input("Qualtos Km você viajou: "))     # PAG = Passagem a pagar
if PAG > 200:
    print(f"Você viajou {PAG:.0f}Km pagara R${PAG*0.45:.2f} reais.")
else:
    print(f"Você viajou {PAG:.0f}Km pagara R${PAG*0.50:.2f} reais.")
print("Volte Sempre!")'''

# Exercicio 4 v2   Usando if simplificado
distancia = float(input('Qual é a distancia viagem? '))
print(f'Vocé está prestes a começar uma viagem de \033[32m{distancia}\033[mKm.')
print("\033[1;37mViajando.....\033[m")
time.sleep(2)
preço = distancia *0.50 if distancia <= 200 else distancia * 0.45  # If simplificado
print(f'O preço da sua passagem será R$\033[1;32m{preço:.2f}\033[m')

# Exercicio 5 Verificar se um ano e bissexto ou não
'''print("--VERIFICADOR ANO BISSEXTO--")
VAB = int(input("Digite ano: "))                   # VAB = Verificador ano bissexto
if VAB % 4 == 0:
    print(f"O ano \033[1;33m{VAB}\033[m é um ano bissexto!")
else:
    print(f"O ano \033[3;33m{VAB}\033[m não é um ano bissexto.")'''
    
# Exercicio 5 v2
ano = int(input('Digite um ano: / Coloque 0 para calcular ano atual: '))
if ano == 0:
    ano = date.today().year        # Verifica ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[35m{ano}\033[m é um ano bissexto.')
else:
    print(f'O ano \033[35m{ano}\033[m não é um ano bissexto.')

# Exercicio 6  Leia tres números mostre qual é maior e qual menor
NB = []
for i in range(3):
    N1 = float(input("Digite valor: "))
    NB.append(N1)      # NB = número bruto
M3 = sum(NB)
print(f"O mair valor sendo \033[30;47m{max(NB):.0f}\033[m.\nO valor menor sendo \033[30;47m{min(NB):.0f}\033[m\nO valor médio sendo \033[7;31m{((sum(NB))/3):.0f}\033[m.")

# Exercicio 7  Salários acima 1.250 aumento 10% é para inferioes ou igual aumento e 15%
print("Calculador de aumento salarial")
S = float(input("Digite o seu sálario: "))
if S <= 1250.00:
    print(f"\033[34mSeu sálario é\033[m \033[33mR${S}\033[m \033[34mreais, com o aumento fica em\033[m \033[4m\033[1;33mR${S+(S*0.15):.2f}\033[m\033[m \033[34mreais.\033[m")
else:
    print(f"\033[34mSeu sálario é\033[m \033[33mR${S}\033[m \033[34mreais, com o aumento fica em\033[m \033[4m\033[1;33mR${S+(S*0.10):.2f}\033[m\033[m \033[34mreais.\033[m")
    
# Exercicio 8     Calcule 3 números veja se pode fazer um Triangulo
print('\033[1;31m-=\033[m'*20)
print('\033[4;31mAnalisador de Triângulo\033[m')
print('\033[1;31m-=\033[m'*20)
r1 = float(input('\033[32mPrimeiro segmento:\033[m '))
r2 = float(input('\033[32mSegundo segmento:\033[m '))
r3 = float(input('\033[32mTerceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;33mOs segmento acima podem formar triângulo!\033[m')
else:
    print('\033[1;33mOs segmentos acima não podem formar triângulo!\033[m')