from os import system
system('cls')

def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)

# Exemplo de uso
escreva('Olá, Mundo!')
escreva('Dev online Python 3')
escreva('Tenha bom dia!')