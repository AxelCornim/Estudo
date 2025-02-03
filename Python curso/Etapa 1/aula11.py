#      Mudança cor de texto          Syle        /    Texto        /     Back
#      \033[syle text  back m        0 None           30 White          40 White
#      \033 [0:   33:  44   m        1 Bold           31 Red            41 Red
#                                    4 Underline      32 Green          42 Green
#                                    7 Negative       33 Yellow         43 Yellow
#       metodo ANSI                                   34 Blue           44 Blue
#                                                     35 Purple         45 Purple
#                                                     36 Ciano          46 Ciano
#                                                     37 Gray           47 Gray

from os import system
system('cls')
 
 # Teste de cores
print("\033[0;30;41m Teste \033[m")
print("\033[4;33;44m Teste \033[m")
print("\033[1;35;44m Teste \033[m")           
print("\033[30;42m Teste \033[m")
print("\033[30;m Teste \033[m")
print("\033[7;30m Teste \033[m")

a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[33m{b}\033[m.')
nome = 'Luan'
cores = {'Limpa':'\033[m', 
         'azul':'\033[34m', 
         "amarelo":'\033[33m', 
         'pretobranco':'\033[7;30m'}
print(f'Olá, {cores["amarelo"]}{nome}{cores["amarelo"]} muito praze em te conhecer!!!')
print(f'Olá, muito prazer te conhecer \033[1;35;40m{nome}\033[m!!!')