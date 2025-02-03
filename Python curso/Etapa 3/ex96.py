from os import system
system('cls')

def area(largura, comprimento):
    return largura * comprimento

print('-'*22 + f'\n{" Controle de Terrenos":^15}\n' + '-'*22)
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

area_terreno = area(largura, comprimento)

print('-'*22)
print(f'A área de um terrreno {largura}x{comprimento} é de {area_terreno} metros quadrados.')