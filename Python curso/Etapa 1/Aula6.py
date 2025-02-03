from os import system
system('cls')

'''NV = []
for i in range(5):s
    N1 = int(input("Digite primeiro número: "))
    NV.append(N1)'''

N1 = int(input("Digite primeiro número: "))
N2 = int(input("Digite segundo número: "))

print('')
S = N1 + N2

print(f'A soma dos 2 valores são: \033[4m\033[1;37;40m{S}\033[m\033[m') 
print(f'Type do primeiro número \033[31m{type (N1)}\033[m é do segundo número \033[1;31m{type (N2)}\033[m') #Identificação do objeto                         # 1
print(f'A soma dos valor \033[0;36;40m{N1}\033[m é do valor \033[36;40m{N2}\033[m resulta em \033[1;36m{S}\033[m quando somados.')   #Forma otimizada usando s-string              # 2
print('A soma do valor \033[34m{0}\033[m é do valor \033[34m{1}\033[m resulta em \033[1m\033[4;34m{2}\033[m\033[m quando somados.'.format(N1, N2, S))  #Forma passada usando .format   # 3
print(f'A soma dos 2 valores são: \033[4m\033[1;37;40{S}\033[m\033[m')                                                                                        # 4
print(float(N1))                                                                                                               # 5
print(bool(N1))                                                                                                                # 6
print(str(N1))                                                                                                                 # 7
print(type(N1))                                                                                                                # 8

N3 = input("Digite Algo: ")
print('isnumeric:', N3.isnumeric())                                                                                          # 9
print('isalpha:', N3.isalpha())                                                                                              # 10
print('isalnum:', N3.isalnum())                                                                                              # 11
print('isupper:', N3.isupper())                                                                                              # 12
print('islower:', N3.islower())                                                                                              # 13