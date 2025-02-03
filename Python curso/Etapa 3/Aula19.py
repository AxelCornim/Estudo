from os import system
system('cls')

# Um dicionario
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'Geoge Lucas'
         }

# Retorna todos valores
print(filme.values()) 
print()

# Retorna todos indices
print(filme.keys())
print()

# Retorna valores e indices
print(filme.items())
print()

# Passa por todos valores e indices
for k, v in filme.items():
    print(f'O {k} é {v}')
print()

pessoa = {'nome': 'Luan', 'sexo': 'M', 'Idade': 19}
print(f'o {pessoa["nome"]} tem {pessoa["Idade"]} anos e do sexo {pessoa["sexo"]}.')

print()
for k, v in pessoa.items():
    print(f'{k} = {v}')