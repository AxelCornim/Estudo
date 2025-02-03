from os import system
system('cls')

"""teste = list()
teste.append('Luan')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])"""

'''galera = [['João', 19], ['Ana', 33], ['Pedro', 48], ['Maria', 55]]
print(galera[2][1])

for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totM = totN = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera) 

system('cls')
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totM += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totN += 1

print(f'Temos {totM} maiores idade é {totN} menores de idade.')