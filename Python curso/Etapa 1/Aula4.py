from os import system
system('cls')

ColorsText = {'clear':'\033[m',
              'blue':'\033[34m',
              'yellow':'\033[33m',
              'red':'\033[31m',
              'purple':'\033[35m',
              'cyan':'\033[36m'}

print('Hello, World!')

print(7+4)

print('7' , '4')  #As aspas fazem virar texto logico vira um objeto

print('Olá' , 5)

N1 = int(input("Número 1 = "))
N2 = int(input("Número 2 = "))
print(f"Soma dos números é {ColorsText['blue']}{N1 + N2}{ColorsText['clear']}")

nome  = input("Qual seu nome?")
idade = input("Qual sua idade?")
peso  = input("Qual seu peso?") 
print(f"O {ColorsText['purple']}{nome}{ColorsText['clear']}, tem {ColorsText['purple']}{idade}{ColorsText['clear']} anos com {ColorsText['purple']}{peso}{ColorsText['clear']}Kg")

nome1 = input("Qual seu nome?")
print(f"Olá {ColorsText['yellow']}{nome1}{ColorsText['clear']}! Bem vindo ao Brasil!")

dia = input("dia = ")
mes = input("mes = ")
ano = input("ano =  ")
print(f"Você nasceu no dia {ColorsText['blue']}{dia}{ColorsText['clear']} de {ColorsText['blue']}{mes}{ColorsText['clear']} de {ano}, correto?")