from random import randint
from math import factorial
from os import system
system('cls')

'''while not X:
    if Y:
        X:
    if Z:
        X:
    if I:
        X:
print(X)'''

'''i = 1
while i < 10:
    print(i)
    i +=1
print('Fim!')'''

'''while i != 0:
    i = int(input('Digite um valor: '))
print('End!')'''

'''i = 'S'
while i == 'S':
    n = int(input('Digite um valor: '))
    i = str(input('Quer continuar? [S/N] ')).upper()
print('End!')'''

'''i = 1
par = impar = 0
while i != 0:
    i = int(input('Digite um valor: '))
    if i != 0:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')'''

# Exercicio 1 / Ler somente valores 'M' ou 'F' caso digite another thing peça novamente para digitar
'''sex = input('Digite sexo: [M/F] ').strip().upper()[0]
while sex not in 'MF':
    print('Informação incorreta, informe seu sexo: ')
print(f'{sex} Registrado com sucesso.')'''

# Exercicio 2 / Refazer desafio 28
'''Machine = randint(0, 10)
acerto = False
erros = 0
cod = 420
print('Adivinhe Número estou pensando de 1 até 10')
while not acerto:
    user = int(input('Resposta --> '))
    if user == Machine:
        acerto = True
        system('cls')
        print(f'\033[32mVocê ganhou! Eu estava pensando {Machine} é você no {user}. Você fez {erros} tentativas.\033[m')
    else:
        if user < Machine:
            print('Dica: pouco mais... Tente novamente.')
        elif user > Machine:
            print('Dica: pouco menos... Tente novamente.')
        erros += 1
        cod += 1
        print(f'{erros} | ERROR {cod} | \n Digite número entre 1 e 10.')'''
        
# Exercicio 3 / Calcule N1 e N2, com base me menu [1] soma [2] multiplicar [3] maior [4] novos números [5] sair programa
'''N1 = int(input('Digite primeiro número: '))
N2 = int(input('Digite segundo número: '))
N3 = []
while N3 != 5:
    print('-=-' *10)
    N3 = int(input(   [1] Soma
   [2] Multiplicar
   [3] Maior
   [4] Novos números
   [5] Sair programa \n--> ))
    print('-=-' *10)
    if N3 == 1:
        print(f'A soma de {N1} e {N2} resulta em {N1+N2}.')
    elif N3 == 2:
        print(f'A multiplicação de {N1} e {N2} tendo resultado {N1*N2}.')
    elif N3 == 3:
        print(f'O maior número entre {N1} e {N2} é {max(N1, N2)}.')
    elif N3 == 4:
        N1 = int(input('Digite primeiro número: '))
        N2 = int(input('Digite segundo número: '))
system('cls')
print(f'Saindo...')'''
# Versão Curta
'''N1,N2,N3 = int(input('Digite primeiro número: ')),int(input('Digite segundo número: ')),[]
while N3 != 5:
 print('-=-' *10)
 N3 = int(input('[1] Soma\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair programa \n--> '))
 print('-=-' *10)
 if N3 == 1: print(f'A soma de {N1} e {N2} resulta em {N1+N2}.')
 elif N3 == 2: print(f'A multiplicação de {N1} e {N2} tendo resultado {N1*N2}.')
 elif N3 == 3: print(f'O maior número entre {N1} e {N2} é {max(N1, N2)}.')
 elif N3 == 4: N1,N2 = int(input('Digite primeiro número: ')),int(input('Digite segundo número: '))
system('cls');print(f'Saindo...')'''
        
# Exercicio 4 / Leia número mostre fatorial
'''while True:
    num = int(input("\033[31mDigite um número para calcular o fatorial:\033[m "))

    if num < 0:
        print("\033[33mO fatorial de números negativos não é definido.\033[m")
        print('')
    elif num == 0 or num == 1:
        print(f"O fatorial de {num} é 1.")
        print('')
    else:
        resultado = 1
        contador = 2

        while contador <= num:
            resultado *= contador
            contador += 1

        print(f"O fatorial de {num} é {resultado}.")
        print('')'''

# Exercicio 5 / Fatorial usando while
'''N1 = int(input('Calculadora Fatorial\n Digite um valor: '))
c = N1
f = 1
print(f'Calculando {N1}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'\033[32mO fatorial de {N1} é {f}.\033[m')'''

# Exercicio 6 / Refazendo 51 usando while 
'''print(' Gerador de PA ')
print('-+' * 10)
P1 = int(input('Primeiro termo: '))
razaoP = int(input('Razão de PA: '))
termo = P1
cont = 1
while cont <= 10:
    print(f'{termo} -> ')
    termo += razaoP
    cont += 1
print('Acabou!')'''

# Exercicio 7 / Refazer PA usando while mostrar 10 primeiro e quantos for nessesario até ponto user pedir
'''print('Gerador de PA')
print('-+' * 10)
P1 = int(input('Primeiro termo: '))
razaoP = int(input('Razão de PA: '))
termo, cont, total, mais = P1, 1, 0, 10
while mais:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razaoP
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos a mais deseja ver? (Digite 0 para encerrar) '))
print(f'Progressão finalizada com {total} termos mostrados.')'''

# Exercicio 8 / Sequencia de Fibonacci
'''print('---' *10)
print(' Sequência de Fibonachi ')
print('---' *10)
termos = int(input('Qualtos termos você quer ver: '))
t1 = 0
t2 = 1
print('===' *10)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Acabou!')
print('===' *10)'''
# Versão Curta SEQEUNCIA DE FIBONACCi
'''print('---' * 10 + '\n Sequência de Fibonacci \n' + '---' * 10)
t1, t2, cont = 0, 1, 3
termos = int(input('Quantos termos você quer ver: '))
print(f'{t1} -> {t2}', end='')
while cont <= termos: t3 = t1 + t2; print(f' -> {t3}', end=''); t1, t2, cont = t2, t3, cont + 1
print(' -> Acabou!\n' + '---' * 10)'''

# Exercicio 9 / O loop continua até que o usuário digite 999 é exibe quantos números foram digitados e qual é a soma deles
'''soma = cont = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [ou 999 para parar]: '))
print(f'Você digitou {cont} números e a soma deles é {soma}.')'''

# Exercicio 10 / Peça user varios números inteiro, user escolhe quando acaba e depois pega média, maior número e menor
'''soma = quantidade = 0
maior = menor = None
while True:
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        maior, menor = max(maior, num), min(menor, num)
    continuar = input('Deseja continuar? [S/N] ')
    if continuar.upper() == 'N':
        break
media = soma / quantidade if quantidade > 0 else 0
print(f'\nVocê digitou {quantidade} números e a média é {media:.0f}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')'''
# Versão Curta 
'''s=q=M=Mn=0
while True:
    try:
        n=int(input('Digite um número: '))
        s+=n;q+=1
        M,Mn=max(M or n,n),min(Mn or n,n)
        if input('Deseja continuar? [S/N] ').upper()=='N': break
    except ValueError:
        break
print(f'Você digitou {q} números e a média é {s/q:.0f}.\nO maior número foi {M} e o menor foi {Mn}.')'''