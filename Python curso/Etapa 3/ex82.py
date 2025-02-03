from os import system
system('cls')

lista1 = list()
par = list()
impar = list()

while True:

    num = int(input('Digite um valor: '))
    lista1.append(num)

    request = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    if request in 'N':
        break

print('=='*30)
print(f'A lista completa sendo {lista1}')
print(f'A lista dos pares é {par}')
print(f'A lista dos impares tendo {impar}')