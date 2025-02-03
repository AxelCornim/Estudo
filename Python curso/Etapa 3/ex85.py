from os import system
system('cls')

impar = list()
par = list()
number = list()
for i in range(1, 8):
    number = int(input(f'Digite o {i} valor: '))
    if number % 2 == 0:
        par.append(number)
    else:
        impar.append(number)

par.sort()
impar.sort()

print('==='*20)
print(f'Os valres pares digitados foram: {par}')
print(f'Os valores ímpares são digitados foram: {impar}')