import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
clear()

def contagem(inicio, fim, passo=1):
    if inicio < fim:
        fim += 1
    else:
        fim -= 1
        passo = -1
    for i in range(inicio, fim, passo):
        print(i, end=' ')
    print('FIM!')
    
contagem(1, 10)
    
contagem(10, 1)

print('=*'*35)

def contagem_com_passo(inicio, fim, passo):
    if inicio > fim and passo > 0:
        passo = -passo
    for i in range(inicio, fim+1, passo):
        print(i, end=' ')
    print('FIM!')
print('Sua vez começar contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passos: '))

contagem_com_passo(inicio, fim, passo)