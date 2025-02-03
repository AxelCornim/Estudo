from os import system
system('cls')

# Definindo a tupla com as palavras
palavras = ('Lápis',
         'Caderno',
         'Estojo',
         'Lapiseira',
         'Compasso',
         'Mochilha',
         'Livro')

'''while True:
    # Iterando sobre as palavras e suas vogais
    for palavra in palavras:
        vogais = 'aeiou'
        vogais_na_palavra = filter(lambda letra: letra in vogais, palavra)
        print(f'Na palavra {palavra} temos as vogais: {", ".join(vogais_na_palavra)}')

    # Perguntando ao usuário se deseja continuar
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break'''
        
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p :
        if letra.lower() in 'aeiou':
            print(letra, end=' ')