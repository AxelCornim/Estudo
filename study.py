import os
os.system('cls')

"""media = []
def tres(media):
    maior = max(media)
    print(f'Número mairo entre {media} foi {maior}')
    return maior, media
    
print('Digite aqui 3 númeoros para ver maior')
while True:
    try:
        if 0 in range(3):
            user = int(input('Digite aqui: '))
            media.insert(user)
            break
    except ValueError:
        print('Digite somente números!!! ')
        
tres = tres(media)"""

def superior(funcionario):
    if funcionario >= 1250:
        aumento = funcionario * 0.10
    else:
        aumento = funcionario * 0.15

    novo_salario = funcionario + aumento
    print(f'Seu salario subiu para ${novo_salario:.2f}Reais.')
    return novo_salario
    
print(' '*4 + 'Veja aqui quanto você vai receber de aumento')
while True:
    try:
        funcionario = float(input('Digite aqui seu salario: '))
        break
    except ValueError:
        print('Digite somente números!!!')
        
novo_salario = superior(funcionario)