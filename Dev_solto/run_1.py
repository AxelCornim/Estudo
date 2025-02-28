from os import system
import math
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

def hipot(n1, n2):
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
print(f'Cosseno aproximado: {cosseno_apo(angulo_radianos):.1f}')