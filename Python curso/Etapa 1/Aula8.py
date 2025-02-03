import pygame
import random
import emoji
import math
from os import system
system("cls")

'''rint(emoji.emojize("Olá, Mundo!:earth_americas:", language='alias'))
print(f"{random.random():.2f}")
print(f"{random.randint(1, 10)}")'''

'''N1 = int(input("Digite um número: "))
Root = math.sqrt(N1)
print(f"A raiz de {N1} é igual a {Root:.2f}")
print(f"A raiz de {N1} é igual a {math.ceil(Root):.2f} arrendondada pra cima.")
print(f"A raiz de {N1} é igual a {math.floor(Root):.2f} arrendondada pra baixo.")'''

# Exercicio 01      Arredondar um número
Num = float(input("Digite um número: "))
print(f"O número arrendodado fica: \033[31m{round(Num)}\033[m")
print(f"Apenas porção inteira fica: \033[1;31m{Num:.0f}\033[m")
print(f"A parte inteira númmero é: \033[7;31m{(int(Num))}\033[m") 

# Exercicio 02      leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
Co = float(input("Comprimento do cateto oposto: "))
Ca = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.sqrt(Co**2 + Ca**2)
print(f"O comprimento da hipotenusa é: \033[4;31m{hipotenusa:.2f}\033[m")

# Exercicio 03     Sorteando nomes
Nome1 = input("Digite nome aluno 1: ")
Nome2 = input("Digite nome aluno 2: ")
Nome3 = input("Digite nome aluno 3: ")
Nome4 = input("Digite nome aluno 4: ")
Sorteado = random.choice([Nome1, Nome2, Nome3, Nome4])
print(f"O aluno escolho é o \033[1m\033[4;31m{Sorteado}\033[m\033[m")

# Exercicio 04     Faz mesma pergunta do 01 mas com uma lista
N1 = str(input("Digite Nome: "))
N2 = str(input("Digite Nome: "))
N3 = str(input("Digite Nome: "))
N4 = str(input("Digite Nome: "))
ListaRoot = N1 + N2 + N3 + N4
Sorteados = []
for i in range(4):
    valor_sorteado = random.choice(ListaRoot)
    Sorteados.append(valor_sorteado)
    ListaRoot = ListaRoot.replace(valor_sorteado, "")
Lista = "\n".join(Sorteados)
print(f"A ordem de aprentação dos trabalhos é:\n\033[3;31m{Lista}\033[m")

#Exercicio 05       seno, cosseno e tangente desse ângulo.
angulo_deg = float(input("Digite o valor do ângulo em graus: "))
angulo_rad = math.radians(angulo_deg)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)
print(f"Seno do ângulo: \033[31;47m{seno:.2f}\033[m")
print(f"Cosseno do ângulo: \033[31;40m{cosseno:.2f}\033[m")
print(f"Tangente do ângulo: \033[1;31m{tangente:.2f}\033[m")

#Exercicio 06     Tocando Mp3
pygame.init()
pygame.mixer.music.load('D:/PC 2/SONS/MACACO.mp3')
pygame.mixer.music.play()
pygame.time.wait(int(3000))
pygame.mixer.music.stop
pygame.quit()