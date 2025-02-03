import os
os.system("cls")

N3 = input("Digite Algo: ")
print('\033[31mÉ um número:\033[m', N3.isnumeric())                                                                            
print('\033[32mÉ letras:\033[m', N3.isalpha())                                                                              
print('\033[33mÉ um alpha númerico:\033[m', N3.isalnum())                                                                           
print('\033[34mEstá em maiusculo:\033[m', N3.isupper())                                                                              
print('\033[35mEstá em minusculo:\033[m', N3.islower()) 
print('\033[36mContem um espaço:\033[m', N3.isspace()) 
print('\033[7;37mÉ do tipo:\033[m',type(N3))                                                                                              
print('\033[7;31mÉ uma questão borleana:\033[m',bool(N3))                                                                                                  
print('\033[7;32mNa string contem:\033[m',str(N3))      
print('\033[7;33mÉ um número real:\033[m',float(N3))                                                                                                   