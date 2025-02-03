from os import system
from random import randint
system('cls')

'''cont = 1
while True:
    print(cont, '-> ', end='')    
    cont += 1
print('Acabou!')'''    # Loop infinito

'''while True:
    pass''' # Crash loop | Isso criará um loop infinito que irá consumir todos os recursos disponíveis.

'''a = []
while True:
    a.append(' ' * 5024)'''  # Aloca 1KB de memória a cada iteração
    
'''def recursion():
    recursion()

recursion()''' #Isso criará uma recursão infinita, consumindo a pilha de chamadas até atingir um erro de estouro de pilha.


'''for cont in range(1, 1000001):
    print(cont, '-> ', end='')    
print('Acabou!')''' # Loop até um milhão # Metodo While

'''for cont in range(1, 1000001):
    print(cont, '-> ', end='')    
print('Acabou!')''' # Metodo for i range():

# Exercicio 1 / Caso digite 999 sai do loop
'''tot = totn = 0
while 1:
    n = int(input('Digite 999 para sair\nDigite número: '))
    if n == 999: break
    tot += n
    totn += 1
print(f'Total de números digitados foi {totn} tendo soma de todos sendo {tot}.')'''

# Exercicio 2 / Faz uma tabuada de acordo que user pedir número
'''print('-=-' *10)
print(' TABUADA 2 ')
print('-=-' *10)
while 1:
    num = int(input('\nDigite número: '))
    if num < 0: break
    if num == 0: break
    for i in range(1, 11):
        print(f'{num} x {i} = {num*i}')
print(' PROGRAMA TABUADAS FINALIZADO! tenha um bom dia.')'''

# Exercicio 3 / Par ou impar quando perder sera contado total vitoria consecutivas
'''v = 0
while True:
    u = int(input('Digite um número: '))
    m = randint(0, 10)
    t = u + m
    tp = ' '
    while tp not in 'PpIi': tp = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {u} e o computador {m}. Total de {t}. ', end='')
    print('Deu par.' if t % 2 == 0 else 'Deu ímpar.')
    if (tp == 'P' and t % 2 == 0) or (tp == 'I' and t % 2 != 0):
        print('Você ganhou!')
        v += 1
    else:
        print('Você perdeu!')
        break
    print('Vamos jogar novamente...')
system('cls')
print(f'GAME OVER!!!\nVocê venceu {v} vezes.')'''

# Exercicio 4 / Leia a idade e o sexo qtd pessoas + 18, qtd homens cadastrados e qtd mulheres < 20 anos
'''maiores_de_18 = mulheres_menos_20 = homens_cadastrados = 0
while True:
    print('---' *9)
    print('   CADASTRE UMA PESSOA')
    print('---' *9)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    print('---' *9)
    if idade > 18:
        maiores_de_18 += 1
    if sexo == 'M':
        homens_cadastrados += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja cadastrar mais uma pessoa? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
print(f'\n{maiores_de_18} pessoa(s) tem mais de 18 anos.')
print(f'Foram cadastrados {homens_cadastrados} homem(ns).')
print(f'{mulheres_menos_20} mulher(es) tem menos de 20 anos.')'''
# Versão Curta
'''m = w = h = 0
while True:
    print('---' * 9 + '\n   CADASTRE UMA PESSOA\n' + '---' * 9)
    i = int(input('Digite a idade: '))
    s = input('Digite o sexo [M/F]: ').upper()
    m += i > 18
    w += s == 'F' and i < 20
    h += s == 'M'
    if 'N' == input('---' * 9 + '\nDeseja cadastrar mais uma pessoa? [S/N] ').upper():
        break
print(f'\n{m} pessoa(s) tem mais de 18 anos.\nForam cadastrados {h} homem(ns).\n{w} mulher(es) tem menos de 20 anos.')'''

# Exercicio 5 / Ler o nome e o preço de vários produtos | total gasto na compra | qtd > 1000 | qual é o nome do produto mais barato
'''total_gasto = produtos_mais_de_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')
print('---' *10)
print('          LOJA BARÂO')
print('---' *10)
while True:
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input(f'Digite o preço do {nome_produto}: R$'))
    total_gasto += preco_produto
    if preco_produto > 1000:
        produtos_mais_de_1000 += 1
    if preco_produto < preco_mais_barato:
        produto_mais_barato = nome_produto
        preco_mais_barato = preco_produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar.upper() == 'N':
        break
print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'Total gasto na compra: R${total_gasto:.2f} reais.')
print(f'Produtos que custam mais de R$1000: {produtos_mais_de_1000}')
print(f'Produto mais barato foi {produto_mais_barato} sendo R${preco_mais_barato:.2f} reais.')'''

# Exercicio 6 / Simular um Caixa Eletrônico
'''print('='*30 + f'\n{"Banco DEV":^30}\n' + '='*30)
valor, total, cedula, total_cedula = int(input('Qual valor você deseja sacar? R$')), 0, 50, 0

while True:
    if valor >= cedula:
        valor -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total deu {total_cedula} cédulas de R${cedula} reais.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        total_cedula = 0
        if valor == 0:
            break

print('='*30 + '\nVolte sempre ao BANCO DEV! Tenha bom dia!')'''