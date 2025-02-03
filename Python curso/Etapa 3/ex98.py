from os import system
system('cls')

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:', flush=True)
    
    if passo > 0:
        if inicio < fim:
            fim += 1
        else:
            fim -= 1
    elif passo < 0:
        if inicio < fim:
            fim -= 1
        else:
            fim += 1
    else:
        print("Erro: O passo não pode ser zero.", flush=True)
        return

    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
    print(flush=True, end=' ')
    print('FIM!')

# Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# Contagem de 10 até 0, de 2 em 2
contador(10, 0, -2)

# Contagem personalizada
contador(int(input("Digite o valor inicial: ")), int(input("Digite o valor final: ")), int(input("Digite o passo: ")))