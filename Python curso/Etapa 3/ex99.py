from time import sleep
from os import system
system('cls')

# função que busca maior
def maior(*núm):
    cont = maior = 0
    print("-=" * 30)
    print("Analisando os valores passados... ")
    for valor in núm:
        print(f"{valor} ", end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"\nForam informados {cont} valores ao todo.")
    print(f"O maior valor informado foi {maior}.")

# Cria uma var
numeros = []

# Resposta usuario
while True:
    n1 = int(input("Digite um número: "))
    numeros.append(n1)

    request = str(input('Deseja continuar? ')).upper().strip()[0]

    # Verifica se usuario responder 'N' acima vai fazer código parar
    if request == 'N':
        system('cls')
        break

maior(*numeros)