from os import	system
system('cls')

L1 = []
for i in range(0, 5):
    L1.append(int(input(f'Digite um valor para a posição {i}: ')))
print('-=-'*15)

maior_valor = max(L1)
menor_valor = min(L1)
indices_maior_valor = [i for i, valor in enumerate(L1) if valor == maior_valor]
indices_menor_valor = [i for i, valor in enumerate(L1) if valor == menor_valor]

print(f'O maior valor foi {maior_valor} na posição {indices_maior_valor}')
print(f'O menor valor foi {menor_valor} na posição {indices_menor_valor}')