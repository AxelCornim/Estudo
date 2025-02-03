from os import system
system('cls')

lanche = ['Burgue', 'Coka', 'Pizza', 'Pudim', 'batata frita']

print(lanche[2])
print(lanche[1:3])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))
print('')

for i in lanche:
    print(i, end='.')

print('\n')
for i in lanche:
    print(f'Eu vou comer {i}')
print('Estou cheio!')

print('\n')
for number, comida in enumerate(lanche): 
    print(f'Eu vou comer {comida} na posição {number}.')

print('\n')
print(sorted(lanche))
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)

c = b + a

print('\n')
print(c)
#print(len(c))
#print(c.count(5))
print(c.index(5, 1))

print('\n')
pessoa = ('Luan', 39, 'M', 60)
print(pessoa)