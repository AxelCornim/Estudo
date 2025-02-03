from os import system
system('cls')
# Criação da Lista
numeros = []
 # Entrada do loop
for num in range(5):
    valor = int(input(f'Digite o {num} valor: '))

    # Verifica se valor for maior que atual e coloca em primeiro    
    if not numeros or valor > numeros[-1]:
        numeros.append(valor)
    else:  # Verifica se valor for menor que ultimo caso for sera adicionado atras substituindo anterior
        for i in range(len(numeros)):
            if valor <= numeros[i]:
                numeros.insert[i, valor]
                break
            
print('-+-'*15)
print(f'Os valores digitados em ordem foram {numeros}')