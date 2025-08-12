from os import system
import random
import math
import time
system('cls')

"""n1 = int(input("Digite valor X: ").strip())
n2 = int(input("Digite valor Y: ").strip())
print(f'Valor de {n1} com {n2} resulta em {n1+n2}')"""

"""def analize(world):
    for i in world:
        if i.isdigit():
            print(f"'{i}' é um número.")
        elif i.isalpha():
            print(f"'{i}' é uma letra.")
        elif i == '.':
            print(f"'{i}' é um ponto decimal (possível parte de um número float).")
        elif i.isspace():
            print(f"'{i}' é um espaço.")
        else:
            print(f"'{i}' é um caractere especial.")
user = input('Digite algo aqui: ')
analize(user)"""

"""var_test = 14
def antepass(nubero):
    global var_test
    ant = nubero - 1
    poss = nubero + 1
    var_test += nubero * 2
    return ant, poss, var_test
user = int(input("Digite aqui para ver seu número antecessor e sucessor: ").strip())
ant, poss, var_test = antepass(user)
print(f'Número antessesor de {user} séria {ant}.')
print(f'Número sucessor de {user} séria {poss}.')
print(f"O valor {user} dividido por 2 vezes é {var_test}. (Um valor inicial de 14 foi somado ao resultado.)")"""

"""def calculor(nuberu):
    trilpe = nuberu*3
    double = nuberu*2
    root = nuberu**0.5
    return trilpe, double, root
user = int(input("Digite um número para ver seu dobro, triplo e raiz quadrada:"))
triple, double, root = calculor(user)
print(f'O dobro de {user} é {double}')
print(f'O triplo de {user} é {triple}')
print(f'Ao quadrado {user} fica {root:.2}')"""

"""def med(a, b):
        return (a + b) / 2
while True:
    try:
        n1 = float(input("Digite primeira nota: "))
        n2 = float(input("Digite segundamente nota: "))
        break
    except ValueError:
        print("Por favor digite somente números!")
media = med(n1, n2)
print(f"Média das notas foi {media}")"""

"""def area(user):
    Cent = user * 100
    Milin = user * 1000
    return Cent, Milin
while True:
    try:
        user = float(input("Digite o valor em metros que deseja converter:"))
        if user >= 0:
            break
        else: 
            print("Digite um valor positivo!")
    except ValueError:
        print("Erro 402. Digite somente números.")
Cent, Milin = area(user)
print(f"{user} metros equivalem:")
print(f"{Cent} centímetros")
print(f"{Milin} milímetros")"""

"""def tabuada(nubero):
    x = 1
    while True:
        y = nubero * x
        print(f'{nubero} x {x} = {y}')
        x += 1
        if x > 10:
            break
    return
user = int(input("Tabuada do --> "))
tabuada(user)"""

"""dollar = 5.8
def money(nuberu):
    global dollar
    valor_convertido = nuberu * dollar
    print(f"Convertendo {nuberu} em dolar fica {valor_convertido:.2f}")
    return valor_convertido
try:
    user = float(input("Digite um número para converter para dolar: "))
    money(user)
except ValueError:
    print("Por favor, Digite somente números! ")"""
    
"""def litrao(l, c):
    area = l * c
    tinta = area/2
    return area,tinta
try:
    comp = float(input("Digite comprimento área: "))
    larg = float(input("Digite largura área: "))
except ValueError:
    print("Digite somente números! ")
area, tinta = litrao(comp, larg)
print(f"Área tem como base {area:.2f} metros quadrados.")
print(f"Serão nessesários {tinta:.2f} litros de tinta para pintar.")"""

"""def desconto(x):
    desconto = 5
    valor_desconto = (desconto / 100) * x   #Posso tambem executar função caso queira somente resultado fazendo
    total_com_desconto = x - valor_desconto #def desconto(x): return x * 0.95
    return total_com_desconto, valor_desconto

# Entrada do usuário
user = float(input("Digite o preço do produto: R$"))

# Cálculo do Desconto
total_com_desconto, valor_desconto = desconto(user) 

# Saída Formatada
system('cls')
print(f"Valor do desconto (5%): R${valor_desconto:.2f}")
print(f"Produto orginal {user:.2f}$ | Preço com desconto: R${total_com_desconto:.2f}")"""

"""def aumento(x):
    return x * 1.15

user = float(input("Digite salário para ver com aumento 25% R$"))   
x = aumento(user)
print(f"Seu sálario com aumento 15% fica R${x:.2f}")"""

""""def temperatura(celsius):
    # Converte celsius para Fahrentheit
    F = (celsius * 9/5) + 32
    return F
# Titulo
print("Conversor Grau Celsius para Grau Fahrenheit")
while True:
    # Input de informação do usuario
    try:
        user = float(input("Digite temperatura em Celsius: "))
        # Output informação com função sendo chamada dentro
        print(f"{user:.1f}°C equivalem {temperatura(user):.1f}°F.")
        break
    # Tratamento de erro
    except ValueError:
        print("Entrada inválida, digite somente números!")"""

"""preco_dia = float(60)
preco_km = float(0.15)
def aluguem_carro(dias, km):
    dia = dias * preco_dia
    km = km * preco_km
    return dia, km
    
while True:
    try:
        km = float(input("Quantos kilometros voçe percorreu: "))
        dia = float(input("Quantos dias voçe percorreu: "))
        break
    except ValueError:
        print("Digite somente números!")
        
dia, km = aluguem_carro(km, dia)
tot = dia + km
print(f"Custo total foi R${tot:.2f}")"""

"""def porcao_inteira(x):
    inteiro = floor(x)
    return inteiro

print((' ' * 2) + "Conversor para porções inteiras")
while True:
    try:
        user = float(input("Digite número: "))
        break
    except ValueError:
        print("Digite somente números!!!")
    
inteiro = porcao_inteira(user)
print(f"A porção inteira de {user} é {inteiro}.")"""

"""def hipotenusa(n1, n2):
    n3 = n1 * n1
    n4 = n2 * n2
    soma_catetos = n3 + n4
    hipot = soma_catetos ** (1/2)
    return hipot
    
while True:
    print(' '*3+'Calculando Hipotenusa')
    try:
        C1 = float(input('Digite primeiro cateto: '))
        C2 = float(input('Digite segundo cateto: '))
        break
    except ValueError:
        print('Digite somente números')

hopott = math.sqrt(C1*C1 + C2*C2)

hipot = hipotenusa(C1, C2)
print(f'Hipotenusa de {C1:.1f} mais {C2:.1f}\nResultando em {hipot:.1f}')
print(f'{hopott:.1f}')"""

"""def hipot(n1, n2):
    # Calcula a hipotenusa de um triângulo retângulo
    return math.hypot(n1, n2)

def factorial(n):
    # Calcula o fatorial de um número
    return 1 if n == 0 else n * factorial(n - 1)

def seno_apo(x, termos=10):
    # Aproxima o seno de x usando a série de Taylor
    seno = 0 
    for n in range(termos):
        termo = ((-1)**n) * (x**(2*n + 1)) / factorial(2*n + 1)
        seno += termo
    return seno
z
def cosseno_apo(x, termos=10):
    # Aproxima o cosseno de x usando a série de Taylor
    cosseno = 0
    for n in range(termos):
        termo = ((-1)**n) * (x**(2*n)) / factorial(2**n)
        cosseno += termo
        return cosseno

while True:
    print(' '*3 + 'Calculos hipotenusa, Seno é Cosseno')
    try:
        cat1 = float(input('Digite Cateto: '))
        cat2 = float(input('Digite outro Cateto: '))
        break
    except ValueError:
        print('Digite somente números')

hipotenusa = hipot(cat1, cat2)
angulo_graus = 30
angulo_radianos = math.radians(angulo_graus)
print(f'Hipotenusa exata: {hipotenusa:.1f}')
print(f'Seno aproximado: {seno_apo(angulo_radianos):.1f}')
print(f'Cosseno aproximado: {cosseno_apo(angulo_radianos):.1f}')"""

"""lista_alunos = list()]
print(" "*3 + "Alunos Sorteados a Apagar quadro")
for i in range(0, 4):
    x = input(str("Digite nome aluno: "))
    lista_alunos.append(x)

aluno_selecionado = random.choice(lista_alunos)
print(f"Aluno Selecionado para limpar quadro foi: {aluno_selecionado}")"""

"""def sorteados(lista_alunos):
    lista_alunos.sort()
    return lista_alunos

lista = []
print("Lista alunos que vão apagar quadro semana")

while True:
    try:
        x = int(input("Digite quantos alunos vão limpar quadro: "))
        for i in range(x):
            y = input(f"{i+1} Digite nome do aluno: ")
            lista.append(y)
        break
    except ValueError:
        print("Digite apenas números!!!")

lista_alunos = sorteados(lista)
print(lista_alunos)"""

"""import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load('Caminho do audio.mp3')

# Reproduz o áudio
pygame.mixer.music.play()

# Mantém o programa rodando enquanto o áudio toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)"""
    
"""def maisculo(texto):
    return texto.upper()

def minusculo(texto):
    return texto.lower()

def total_letras(texto):
    return len(texto)

def letras_primeiro(texto):
    return len(texto.split()[0])

while True:
    try:
        user = str(input("Digite seu nome completo: "))
        break
    except ValueError:
        print('Digite somente nomes!! ')
        
print(f"Seu nome maiúsculo fica {maisculo(user)}")
print(f"Seu nome minúsculo fica {minusculo(user)}")
print(f'Ao todo seu nome tem {total_letras(user)} letras')
print(f"Seu primeiro é {user.split()[0]} é tem {letras_primeiro(user)} letras")"""

"""def leitura(numeros):
    # prenche número para não aja erros de faltar autofill
    numero_prenchido = numeros.zfill(4)
    x1 = numero_prenchido[0]
    x2 = numero_prenchido[1]
    x3 = numero_prenchido[2]
    x4 = numero_prenchido[3]
    return x1, x2, x3, x4

# Loop para certificar usuario de digitar somente números de 0 até 9999
while True:
    try:
        user = input('Informe número 0-9999:  ')
        if user.isdigit() and 0 <= int(user) <= 9999:
            break
    except ValueError:
        print("digite somente números!!!")
        
# Chamando a função
x1, x2, x3, x4 = leitura(user)

# Output da mensagem
print(f"Analizando número {user}")
print(f"Milhar: {x1}")
print(f"Centena: {x2}")
print(f"Dezena: {x3}")
print(f"Unidade: {x4}")"""

"""def santis(cidade):
    cidade = cidade.upper()
    nome_cidade = "SANTOS" in cidade
    return nome_cidade

while True:
    try:
        user = str(input("Digite nome sua cidade: "))
        break
    except ValueError:
        print('Digite somente nomes com letras!!! ')
        
nome_cidade = santis(user)

print(nome_cidade)
"""

"""def sobrenome(nome): 
    nome = nome.upper()
    silva = 'SILVA' in nome
    return silva

while True:
    print(''*3 + 'Verificador se contém nome Silva')
    try:
        user = str(input('Digite seu nome completo: '))
        break
    except ValueError:
        print('Digite somente nomes!!! ')

silva = sobrenome(user)
if silva == True:
    print(f"Nome {user} contém no nome Silva.")
else:
    print(f'Nome {user} não contém Silva no nome.')"""

"""def tot_a(letras):
    texto_maiusculo = letras.upper()
    tot_letrasA = texto_maiusculo.count("A")
    primeiroA = texto_maiusculo.find("A")
    ultimoA = texto_maiusculo.rfind("A")
    return tot_letrasA, primeiroA, ultimoA

while True:
    try:
        user = str(input("Digite uma frase: "))
        break
    except ValueError:
        print('Digite somente frases com letras!!! ')
        
tot_letrasA, primeiroA, ultimoA = tot_a(user)

if tot_letrasA > 0:
    print(f'Na frase tem total {tot_letrasA} letras A.')
    print(f'Primeira letras A aparece no index {primeiroA+1}')
    print(f'Última letra A aparece no index {ultimoA+1}')
elif tot_letrasA >= 0:
    print('Na frase não contém letras A.')"""

"""def first_name(nomecompleto):
    partes = nomecompleto.split()
    return partes[0] if partes else 'Nome invalido' 

nome = []
while True:
    try:
        user = str(input('Digite seu nome: ')).strip()
        if user and ' ' in user:
            nome.append(user)
        break
    except ValueError:
        print('Digite somente nomes com letras!!! ')
    
primeiro_nome = first_name(nome[0]) if  nome else 'Nenhum nome fornecido'

print(f'\nNome completo: {user}')
print(f'Seu primeiro nome é {primeiro_nome}')"""

"""def carregando(pontos=3, espera=0.7):
    print("Aguarde", end="", flush=True)
    for _ in range(pontos):
        time.sleep(espera)
        print(".", end="", flush=True)
    print()  # quebra de linha final

def sorteando(user):
    sorteando = random.randint(0, 5)
    if sorteando == user:
        carregando()
        system('cls')
        print(f'Parabens voce acertou! Número era {sorteando}')
    elif sorteando > user or sorteando < user:
        carregando()
        system('cls')
        print(f'Voce chegou perto, errou por {sorteando - user}\n Número certo era {sorteando}\n Seu palpite foi {user}')
    return sorteando 
        
while True:
    print(' '*3 + 'Sorteando Números\nVocê consegue acertar ?')
    try:
        user = int(input('Digite um número de 0/5: '))
        if 0 <= user <= 5:
            break
    except ValueError:
        print('Digite somente números!!!')
        
sorteando = sorteando(user)"""

"""def calcular_multa(velocidade):
    if velocidade > 80:
        excesso = velocidade - 80
        valor_multa = excesso * 7.00
        print(f'Você foi multado em R${valor_multa:.2f}.\nPassou {excesso:.2f} km/h acima do limite permitido.')
        return excesso, valor_multa # Retorna multa se houver
    else:
        print(f'Você passou a Km/h {velocidade:.2f}\n Boa viagem!')
        return None, None # Retorna nada sem multas

while True:
    try:
        velocidade = float(input('Digite Sua velocidade (Km/h): '))
        system('cls')
        excesso, multa = calcular_multa(velocidade)
        break
    except ValueError:
        print('Digite somente velocidade usando números!!!')"""

"""def par_impar(user):
    if user % 2 == 0:
        print(f'Número {user} é par!')
    else:
        print(f'Número {user} é impar!')
    return user

print(' '*3 + 'Verificador de númeors pares é impares')
while True:
    try:
        entrada = int(input('Digite um número (inteiro): '))
        break
    except ValueError:
        print('Digite somente números!!!')
        
system('cls')
par_impar = par_impar(entrada)"""

"""def viagem(carro):
    if carro <= 200:
        valor_corrida = carro * 0.5
        print(f'Valor da corrida ficou em ${valor_corrida:.2f}Reais')
    elif carro > 200:
        valor_corrida = carro * 0.45
        print(f'Para distancias mais longas temos desconto 5%\nFicou ${valor_corrida:.2f}Reais.')
    return valor_corrida, carro
        
print(' '*7 + 'Uber')
while True:
    try:
        motorista = float(input('Quantos Km\h foi percorrido: '))
        break
    except ValueError:
        print('Digite somente números!!!')
        
viagem = viagem(motorista)"""

"""def verificador_bissexto(ano):
    system('cls')
    print(' '*4 + 'Verificador ano bissexto')
    if ano % 4 == 0:
        print(f'{ano} é bissexto.')
    else:
        print(f'{ano} não é bissexto!')
    return ano

print(' '*4 + 'Verificador ano bissexto')
while True:
    try:
        user = int(input('Digite aqui --> '))       
        break
    except ValueError:
        print('Digite somente números inteiros, e somente númeoros!!!')
        
verificador_bissexto = verificador_bissexto(user)"""

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

"""def superior(funcionario):
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
        
novo_salario = superior(funcionario)"""

"""def triangulo(esquerdo, direito, base):
    soma_lados = esquerdo + direito
    if esquerdo + direito > base and esquerdo + base > direito and direito + base > esquerdo:
        print('Com dados fornecidos formase um triângulo.')
        return soma_lados
    else:
        print('Com dados fornecidos não se forma um triângulo.')
    
while True:
    try:
        esquerdo = int(input('Lado esquerdo: '))
        direito = int(input('Lado direto: '))
        base = int(input('Base: '))
        break
    except ValueError:
        print('Digite somente números!!!')
        
triangulo = triangulo(esquerdo, direito, base)"""

"""def emprestimo(valor_pedido, anos, salario):
    valor_mes = valor_pedido / (anos*12)
    valor_parcela = salario * 0.30
    if valor_mes > valor_parcela:
        print('O emprestimo foi Negado!')   
    else:
        print('Parabens seu emprestimo foi APROVADO!')
    return valor_mes, valor_parcela
        
print(' '*3+'Banco Central da Mentira')
print('='*30)

while True:
    try:
        salario = int(input('Digite seu salario: '))
        valor_pedido = int(input('Digite valor deseja o emprestimo: '))
        anos = int(input('Em quantos anos deseja pagar: '))
        break
    except ValueError:
        print('Por favor digite somente números!!!')
        
valor_mes, valor_parcela = emprestimo(valor_pedido, anos, salario)"""

"""def conversor_01(inteiro): # Caso queira conversao limpa pode usar
    binario = bin(inteiro) # isto para remover prefixos [2:]
    octal = oct(inteiro)
    hexadecimal = hex(inteiro)
    return binario, octal, hexadecimal

print(' '*3+'Conversor de binário, octal e para hexadecimal')
print('='*30)

while True:
    try:
        inteiro = int(input('Escreva aqui: '))
        break
    except ValueError:
        print('Digite somente números inteiros!!!')
        
while True:
    try:
        repeat = int(input('Digite 1 para binário | 2 para octal | 3 para hexadecimal\n(Digite 999 para sair)'))
        if repeat == 1:
            binario = conversor_01(inteiro)
            print(f'{inteiro} Convertido para binário {binario[0]}')
        elif repeat == 2:
            octal = conversor_01(inteiro)
            print(f'{inteiro} Convertido para octal {octal[1]}')
        elif repeat == 3:
            hexadecimal = conversor_01(inteiro)
            print(f'{inteiro} Convertido para hexadecimal {hexadecimal[2]}')
        elif repeat == 999:
            print('Programa encerado!')
            break
    except ValueError:
        print('Escreve só números!!!')"""
        

"""from statistics import mean, median

dados = []
def valores(casa):
    maior_num = max(casa)
    minimo_num = min(casa)
    if casa[0] == casa[1]:
        print(f'Os números são iguais: {casa[0]}x{casa[1]}')
    print(f'Maior número foi {maior_num}\nTendo seu menor número sendo {minimo_num}')
    return maior_num, minimo_num

while True:
    try:
        for i in range(0, 2):
           numeros = int(input(f'({i}) Digite um número: '))
           dados.append(numeros)
        break
    except ValueError:
        print('Digite somente números! ')
        
valores = valores(dados)"""

"""from datetime import datetime    
                                                   
def alistamento(nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    if idade > 18:
        print(f'Você está atrasado em {idade - 18} anos para alistamento!')
    elif idade < 18:
        print(f'Ainda falta {18 - idade} anos para se alistar.')
    elif idade == 18:
        print(f'Você chegou momento correto para se alistar!')
    return idade, ano_atual

print(' '*3 + 'Alistamento Militar')
print('='*30)

while True:
    try:
        nascimento = int(input('Ano que nasceu: '))
        break
    except ValueError:
        print('Erros 404\nTente Novamente!')        
        
alistamento = alistamento(nascimento)"""

"""def media_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 5 or media <= 6.9:
        print(f'Você ficou em recuperação: Sua nota {media:.2f}')
    elif media < 5:
        print(f'Você foi REPROVADO!! Sua nota {media:.1f}')
    elif media >= 7:
        print(f'Você foi APROVADO!!! Sua nota {media:.1f}')
    return media

print(' '*3 + 'Boletin Escolar')
print('='*30)

while True:
    try:
        nota1 = float(input('Digite sua primeira nota: '))
        nota2 = float(input('Digite sua segunda nota: '))
        break
    except ValueError:
        print('Erro tente novamente!!!')
        
media_notas = media_notas(nota1, nota2)""" 

"""from datetime import datetime

def avaliador(nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    if idade <= 9:
        print('Você está categoria Mirim!') 
    elif 10 <= idade <= 14:  
        print('Você está categoria Infantil!')
    elif 15 <= idade <= 19:
        print('Você está na categoria Júnior!')
    elif 20 <= idade <= 25: 
        print('Você está na categoria Sênior!')
    elif idade > 25:
        print('Você está na categoria Mestre!')
    return ano_atual, idade

print(' '*3 + 'A Confederação Nacional de Natação')
print('='*30)

while True:
    try:
        nascimento = int(input('Digite data do seu nascimento: '))
        break
    except ValueError:
        print('Error!! Tente Novamente: ')
        
avaliador = avaliador(nascimento)"""

"""def formas_triangulo(primeiro, segundo, terceiro):
    if primeiro == segundo == terceiro:
        print('Com dados fornecidos formase um equilátero.')
    elif primeiro == segundo or primeiro == terceiro or segundo == terceiro:
        print('Com dados fornecidos formase um isósceles.')
    else:
        print('Com dados fornecidos formase um escaleno.')
    return 

print(' '*3 + 'AngleJudge')
print('='*30)

while True:
    try:
        primeiro = int(input('Primeiro lado: '))
        segundo = int(input('Segundo lado: '))
        terceiro = int(input('Terceiro lado: '))
        break
    except ValueError:
        print('Errado!!! Tente Novamente: ')
        
formas_triangulo = formas_triangulo(primeiro, segundo, terceiro)"""

"""def imc(peso, altura):
    altura_real = altura ** 2
    imc = peso / altura_real
    if imc <= 18.5:
        print(f'[{imc:.1f}]Você está abaixo do peso.')
    elif 18.5 <= imc <= 25:
        print(f'[{imc:.1f}]Seu peso está ideal.')
    elif 25 <= imc <= 30:
        print(f'[{imc:.1f}]Você com sobrepeso.')
    elif 30 <= imc <= 40:
        print(f'[{imc:.1f}]Você está obeso.')
    elif imc >= 40:
        print(f'[{imc:.1f}]Você está com obesidade mórbidda.')
    return imc, altura_real

print(' '*4 + 'Calculadora do IMC')
print('-~-'*10)

while True:
    try:
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: '))
        # Verifica se são valores positivos
        if peso <= 0 or altura <= 0:
            raise ValueError('Peso e altura devem ser maiores que zero.')
        break
    except ValueError as e:
        # Aqui pegamos tanto erros de conversão quanto nosso ValueError customizado
        print(f'Entrada inválida: {e}\nPor favor, tente novamente.')
    except Exception as e:
        # Qualquer outro erro inesperado
        print(f'Erro inesperado: {e}\nTente novamente.')
        
imc = imc(peso, altura)"""

"""def pagamento(valor):
    avista = valor * 0.90
    cartao_avista = valor * 0.95
    cartao_duasX = valor
    cartao_tresX = valor * 1.20
    return avista, cartao_avista, cartao_duasX, cartao_tresX

print(' '*3 + 'Loja de Roupas Ligeiro')
print('-=-'*10)

while True:
    try:
        valor = float(input('Digite valor produto: '))
        break
    except ValueError:
        print('ERROR CÓDIGO 404\nTente novamente! ')

avista, cartao_avista, cartao_duasX, cartao_tresX = pagamento(valor)

while True:
    try:
        usuario = int(input('[1] à vista dinheiro/cheque'
                            '\n[2] à vista cartão'
                            '\n[3] 2x no cartão'
                            '\n[4] 3x ou mais no cartão'
                            '\n[5] Para sair'
                            '\n Qual opção senhor escolhe?'
                            '\n---> '
                            ))
        if usuario == 1:
            print(f'A vista o valor sua compra fica R${avista:.2f}Reais.')
        elif usuario == 2:
            print(f'O valor a vista no cartão fica R${cartao_avista:.2f}Reais.')
        elif usuario == 3:
            print(f'Duas vezes no cartão valor da compra fica R${cartao_duasX:.2f}Reais.')
        elif usuario == 4:
            print(f'Três vezes no cartão ficou com juros de %5 R${cartao_tresX:.2f}Reais.')
        elif usuario == 5:
            print('Programa Finalizado!')
            break
    except ValueError: 
        print('Digite somente valores dentro tabela! ')"""
        
"""from random import choice
        
maquina = [1, 2, 3]
        
def jokenpo(jogador, maquina):
    maquina = choice(maquina)
    if jogador == maquina:
        return 'Empate!'
    elif (jogador == 1 and maquina == 3) or \
         (jogador == 2 and maquina == 1) or \
         (jogador == 3 and maquina == 2):
        return 'Você venceu!'
    else:
        return 'Máquina venceu!'
    
opcoes = {1: 'pedra', 2: 'papel',3: 'tesoura'}

try:
    jogador = int(input('Escolha: 1 (Pedra), 2 (Papel), 3 (Tesoura): '))
    if jogador not in opcoes:
        print('Escolha inválida')
    else:
        print(f' Você escolheu {opcoes}{jogador}')
        print(f'Máquina escolheu {opcoes}{maquina}')
        print(jokenpo(jogador, maquina))
except  ValueError:
    print('Digite somente números inteiros!!! ')"""
    
"""from time import sleep

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    
print('Vish estorou tudo!')"""  

"""for i in range(0, 51):
    if i % 2 == 0:
        print(i, end=' ')"""

"""multiplo_tres = 0
qtd = 0
        
for i in range(1, 501):
    if i % 3 == 0 and i % 2 == 1:
        qtd += 1
        multiplo_tres += i
  
print(f'Todos númeors multiplicaveis por três são {qtd} e deu total {multiplo_tres}')"""

"""print(' '*15 + 'Tabuada')
print('-~'*20)

while True:
    try:
        entrada = int(input('Digite número deseja ver tabuada: '))
        for i in range(1, 11, 1):
            print(f'{entrada} x {i} = {entrada*i}')
        break
    except ValueError:
        print('Entrada inválida!\n Tente novamente: ')"""
          
"""from os import system
                
print(' '* 3 + 'Soma de Pares (ímpares serão ignorados)')
print('-+-'*15 + '\nDigite [0] para sair do loop')

soma_pares = 0

while True:
    try:
        entrada = int(input('Digite aqui: '))
        if entrada % 2 == 0:
            soma_pares = entrada + soma_pares
        if entrada == 0:
            break
    except ValueError:
        print('Entrada inválida!\nTente novamente: ')
        
system('cls')
print(f'Soma de todos pares foi {soma_pares}')"""
        
"""print('='*30 + '\n10 Termos de uma PA'+ '\n' + '='*30)
        
while True:
    try:
        primeiro_termo = int(input('Primeiro termo: '))
        razao = int(input('Razão: '))
        break
    except ValueError:
        print('Entrada inválida!\nTente Novamente: ')
        
def pa(primeiro_termo, razao):
    print(primeiro_termo, end=' -> ')
    termo = primeiro_termo
    for i in range(0, 9):
        termo += razao
        print(termo, end=' -> ')
    print(end='Acabou !')
    return termo    
    
pa(primeiro_termo, razao)"""

"""print('-~'*30)
print(' '*15 + 'Verificador de números primos')
print('-~'*30)

while True:
    try:
        n = int(input('Digite número aqui: '))
        break
    except ValueError:
        print('Erro 403!\nTente novamente: ')
        
print(f'{n} é primo.' if n > 1 and all(n % i for i in range(2, int(n**0.5) + 1)) else f'{n} não é primo!')"""

