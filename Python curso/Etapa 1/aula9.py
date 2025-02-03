from os import system
system("cls")

#frase = str('Curso em vídeo Python')

# Fatiamento
'''print(frase[::2])
print(frase[9])              # Mostra somento letra com base no indice mostrado
print(frase[9:13])           # Começar no 9 termina no 12 pois 13 e uma borda é bordas não são contadas
print(frase[9:21])           # Está de forma inadequada pois está fora da contagem existente de indices
print(frase[9:21:2])         # Começa 9 vai pulando 2 em dois, nesses casos pula primeiro mostra segundo
print(frase[:5])             # Quando omite começo so coloca indice final vai do começo até 5
print(frase[15:])            # Vai de 15 até um final que não se sabe onde acaba
print(frase[9::3])'''            # Começa nove vai pulando 3 em 3 até um final que foi omitido

# Analize
'''print(len(frase))                   # len = comprimento, mostra total caracteres
print(frase.count('o'))             # Contagem qualtas X aparece Y na frase
print(frase.count('o', 0, 13))      # Padrão seria  Frase[Começo:fim:passos] mas um número ou letra querendo ser identificada fica sendo Frase[obj:Começo:fim]
print(frase.find('deo'))            # indica pelo indice onde começa oque está dentro ' '
print(frase.find('android'))        # Vai dar output de -1 pois não foi encontrado palavra 'Android'
print('Curso' in frase)'''             # Condição boorleana 1 existe 0 não existe 'Curso' na frase

# Transformação
'''frase.replace('Python', 'Android')      # Substitui a letra de forma segundaria frasa.replace['Letra a ser subtituida', 'Subtuto']
frase.upper()                           # Deixa tudo em maisculo 
frase.lower()                           # Deixa tudo em minusculo
frase.capitalize()                      # Deixa somente primeira letra maisculo resto em minusculo
frase.title()                           # Vai todas palavras em maiusculos 
frase.strip()                           # Remove todos espaços inuteis
frase.rstrip()                          # Vai tratar var somente lado direito por isso 'Rstrip'
frase.lstrip()'''                          # Vai tratar somente lado esquerdo

# Divisão
'''print(frase.split())           # Onde tiver espaço em vazio vai dividir, assim criando para cada espaço uma nova var com um novo indice. Exemplo ([Curso] = 0 [em] = 1 [Video] = 2 [Python] = 3)
frasediv = frase.split()
print(frasediv[2][3])'''
# Junção/Concactenação
#'-'.join(frase)         # Com uma concactenação feita dessa forma [Curso-em-Video-Pyton] pois oq está dentro ' ' sera colocado na hora junção

# Forma inacada do exercicio 2
'''N = str(Num)
print(f"Unidade {3}")
print(f"Dezena: {2}")
print(f"Centena: {1}")
print(f"Milhar: {0}")'''

# Exercicio 1         Ler nome completo mostrar upper, lower e qualtas letras contem sem espaços é quantas letras tem primeiro nome.
Nome = str(input("Qual seu nome? "))
print(f"Seu nome com tudo maiúsculo fica \033[35m{Nome.upper()}\033[m.")
print(f"Seu nome com tudo minúsculo fica \033[1;35m{Nome.lower()}\033[m.")
print(f"Seu nome tem \033[3;35m{len(''.join(Nome.split()))}\033[m")
print(f"Seu primeiro nome tem \033[4;35m{len((Nome.split()))}\033[m letras.")

# Exercicio 2     Leitor Unidade, dezena, centena e milhar
Num = int(input("Digite um número: "))
u = Num // 1 % 10
d = Num // 10 % 10
c = Num // 100 % 100
m = Num // 1000 % 1000
print(f"Unidade \033[33m{u}\033[m")
print(f"Dezena: \033[34m{d}\033[m")
print(f"Centena: \033[32m{c}\033[m")
print(f"Milhar: \033[31m{m}\033[m")

# Exercicio 3    Ler nome cidade dizer se tem "Silva" ou não no começo do nome
Cidade = str(input("Qual nome da sua cidade? "))
SANTO = Cidade.lower().split()
if SANTO[0] == 'Silva':
    print(f"A cidade \033[1;31m{Cidade}\033[m começa com nome \033[31mSanto\033[m.")
else:
    print(f"A cidade \033[31m{Cidade}\033[m não começa com nome \033[1\033[4;31mSanto\033[m\033[m.")
    
# Exercicio 4    Ler nome dizer se contem Silva nele
Nome = str(input("Qual seu nome completo? "))
NEM = Nome.lower()            # NCS = Nome em Minusculo
if 'silva' in NEM:
    print(f"O nome \033[1;35m{Nome}\033[m contém \033[1m\033[4;35mSilva\033[m\033[m incluso ao nome.")
else:
    print(f"O nome \033[4;35m{Nome}\033[m não contém \033[4\033[1;35mSilva\033[m\033[m incluso ao nome.")
    
# Exercicio 5   Qualtas X aparece letra A, em que posição aparece primeiro A é que posição aparece ultima vez.
Frase = str(input("Qual sua frase? "))
CA = Frase.lower().count('a')  # CA = Contagem A
CLA = Frase.lower()            # CLA = Contagem letra A 
print(f"Aparece \033[7;36;43m{CA}\033[m vezes letra \033[33m'A'\033[m vezes na frase.")
if 'a' in CLA:
    print(f"A frase \033[33m{Frase}\033[m, contém a primeira letra \033[4m\033[1;33m'A'\033[m\033[m, que aparece no índice \033[1;33m{CLA.find('a')}\033[m.")
    print(f"A frase \033[33m{Frase}\033[m, contém a última letra \033[4m\033[1;33m'A'\033[m\033[m, que aparece no índice \033[1;33m{CLA.rfind('a')}\033[m.")
else:
    print(f"A frase \033[4;31m{Frase}\033[m, não contém letra \033[1;33m'A'\033[m.")
    
# Exercicio 6   Leia uma frase mostre primeira e ultima letra,
Nome = str(input("Digite seu nome completo: "))
NCM  = Nome.split()       # NCM = Nome com modificações
print(f"Seu nome completo é \033[1;30;47m{Nome}\033[m, começando com \033[33m{NCM[0]}\033[m é tendo seu ultimo nome sendo \033[7;33;47m{NCM[-1]}\033[m.")