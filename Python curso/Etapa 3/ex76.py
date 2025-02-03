from os import system
system('cls')

lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Lapiseira', 4.20,
         'Compasso', 9.99,
         'Mochilha', 120.32,
         'Livro', 34.90)
print('='*40)
print(f'{"Lista de produtos":^40}')
print('='*40)
for i in range(0, len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}', end='')
    else:
        print(f'R${lista[i]:>7.2f}')
print('='*40)