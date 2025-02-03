from random import randint
from os import system
system('cls')

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os números aleatório gerados foram: ', end='')

for i in numeros:
    print(f'{i}', end=' ')

print(f'\nO menor valor é: {min(numeros)}')
print(f'O maior valor é: {max(numeros)}')