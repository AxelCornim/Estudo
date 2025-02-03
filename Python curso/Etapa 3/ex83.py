from os import system
system('cls')

while True:
    expressao = input('Digite uma expressão com parênteses: ')

    pilha = []

    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
        elif caractere == ')':
            if not pilha:
                print('Os parênteses não estão corretamente balanceados.')
                break
            pilha.pop()
    else:
        if not pilha:
            print('Os parênteses estão corretamente balanceados.')
        else:
            print('Os parênteses não estão corretamente balanceados.')