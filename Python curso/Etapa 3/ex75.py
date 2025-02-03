from os import system
system('cls')

# Lendo os valores e criando a tupla
valores = tuple(int(input(f'Digite o {i+1}º valor: ')) for i in range(4))

# Contando quantas vezes o valor 9 aparece
aparicoes_9 = valores.count(9)

# Encontrando a posição do primeiro 3 (se existir)
pos_primeiro_3 = valores.index(3) if 3 in valores else None

# Encontrando os números pares
pares = [valor for valor in valores if valor % 2 == 0]

# Mostrando os resultados
print(f'O valor 9 apareceu {aparicoes_9} vezes.')

if pos_primeiro_3 is not None:
    print(f'O primeiro valor 3 foi digitado na posição {pos_primeiro_3 + 1}.')
else:
    print('O valor 3 não foi digitado.')
    
print(f'Os números pares digitados foram: {pares}')