from os import system 
system('cls')

# Tabuada em For i range(1, 11)
'''print('='*30 + f'\n{"TABUDADA":^30}\n' + '='*30)
N1 = int(input('Digite número: '))
for i in range(1, 11):
    print(f'{N1} x {i} = {N1*i}')'''
    
# Calculadora números pares inteiros
'''print('-=-'*10 + f'\n{"SOMADORA DE PARES":^30}\n' + '-=-'*10)
PV = int(input('Qualtas vezes deseja somar: '))
PV += 1
par = 0
impar = 0

for i in range(1, PV):
    N1 = int(input(f'Digite {i} valor: '))
    if N1 % 2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'Existe \033[32m{par}\033[m números pares é \033[35m{impar}\033[m números impares.')'''

# Calcular fatorial
'''print(f'\033[33m{"Calculador de Fatorias":^15}\033[m')

N1 = int(input('Qual número deseja calcular --> '))

fac = 1
for i in range(1, N1 + 1):
    fac *= i
    
print(f'O fatorial de \033[32m{N1}\033[m é \033[1;32m{fac}\033[m.')'''

# Faz uma repetição até var 'i' ter mesmo valor ou inferior a var 'N1' 
'''while True:
    N1 = int(input('Digite um número: '))

    for i in range(1, N1 + 1):
        print(i, end=' ')
        i += 1

    request = str(input('\nDeseja continuar? (S/N) ')).upper().strip()[0]

    # Verificar a var 'request' se for igual N quebra, se for igual S continua, se for digitado clear e limpado prompt e fro digado qualquer
    # outra coisa e relevado como invalido. 
    if request == 'N':
        break
    elif request == 'S':
        continue
    elif request in 'CLEARclearClear':
        system('cls')
        system('clear')
    else:
        print('Opção inválida. Por favor, digite S para continuar ou N para sair.')

print()
print('~' *30 + f'\n{"ACABOU!":^30}\n' + '~' *30)'''

# Tabela de funções math
'''n1 = int(input("Digite primeiro valor: "))
n2 = int(input("Digite segundo valor: "))
system('cls')
while True:
    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa""")
    request = int(input())
    if request == 1:
        print(f"A soma de {n1} e {n2}: {n1+n2}")
    elif request == 2:
        print(f"A multiplicação de {n1} e {n2}: {n1*n2}")
    elif request == 3:
        print(f"Número maior é {max(n1, n2)}.")
    elif request == 4:
        n1 = int(input("Digite primeiro valor: "))
        n2 = int(input("Digite segundo valor: "))
    elif request == 5:
        system('cls')
        print('='*30 +f"\n{'PROGRAMA FINALIZADO!':^30}\n" + '='*30)
        break
    else:
        print('Digitar valores da tabela.')'''

# Calculadora de Fatorial
'''fac = 1
n1 = int(input("Digite valor do fatorial: "))
if n1 > 0:
    print(f"{n1}! =", end=' ')
    for n in range(n1, -1, -1):
        fac *= n
        if n != 1:
            print(n, end=' x ')
        else:
            print(' =', fac)
            break'''

# Adivinhação de Números
'''from random import randint
print('='*30 + f"\n{'JOGO DA ADIVINHAÇÂO':^30}\n" + '='*30)
machine = randint(1,10)
attempts = 0
while True:
    user = int(input("Digite um valor de 1 até 10: "))
    attempts += 1
    if user == machine:
        break
    elif user > machine:
        print("Dica: Tente pouco mais baixo.")
    else:
        print("Dica: Tente número alto.")
print(f"\n\033[32mVocê ganhou!!!\033[m\n\033[1;31mCom apenas {attempts} tentativas.\033[m")'''

# Número por extenso 
'''números_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 
    'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
)

while True:
    user = int(input("Digite valor entre 0/20: "))
    print(f'O valor por extenso é {números_extenso[user]}')
    resp = str(input(f'Deseja continuar? ')).upper().strip()[0]
    if resp in 'N':
        break
print('=' * 30 + f"\n{'ACABOU!!!':^30}\n" + '=' * 30)'''

# Média de Notas
'''notas = []
while True:
    user = float(input("Nota do aluno: "))
    notas += (user,)
    request = str(input("Deseja continuar? ")).upper().strip()[0]
    if request in 'N':
        break

system('cls')
media = sum(notas) / len(notas)
if media > 0:
    print(f"A média foi {media:.2f}.")
else:
    print(f"Sua média foi {media:.2f}")'''

# Cadastro de alunos
'''print(f"{'Cadastro De Alunos':^20}\n"+'-'*20)
lista_alunos = []
while True:
    nome = str(input("Digite nome: "))
    nota = float(input("Digite a nota: "))

    lista_alunos.append((nome, nota))

    request = str(input("\nDeseja continuar?")).upper().strip()[0]
    print()
    if request in 'N':
        break

print(f"{'Alunos Cadastrados':^30}\n"+'-'*30)
for nome, nota in lista_alunos:
    print(f"Nome: {nome:^1}, Nota: {nota:.1f}")'''

# 