from os import system
system('cls')

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 7 in num:
    num.remove(7)
else:
    print('Não achei número 7')
print(num)
print(f'Lista contém {len(num)} elementos.')

V1 = list()
for user in range(0, 5):
    V1.append(int(input('Digite um valor: ')))
V1.append(5)
V1.append(9)
V1.append(7)

for i, V1 in enumerate(V1):
    print(f'Posição {i} encontrei valor {V1}.')
print('End List!')

a = [2, 3, 4, 7]
b = a[:]          # Copia de valores para lista B
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')