from random import randint
from os import system
system('cls')

def sorteia(lista):
    print("Sorteando 5 valores para a lista:", end=" ")
    for _ in range(5):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=" ", flush=True)
    print("PRONTO!")

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"A soma dos valores pares de {lista} é {soma}.")

# Lista para armazenar os números sorteados
numeros = []

# Chamando a função sorteia
sorteia(numeros)

# Chamando a função somaPar
somaPar(numeros)