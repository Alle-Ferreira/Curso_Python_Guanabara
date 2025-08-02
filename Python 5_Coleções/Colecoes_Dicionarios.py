'''COMPARATIVO

Variavel Simples()			                    mutavel
Variavel Composta: Tupla()				        imutavel    posicional
lista = list()	            lista[]		        mutavel     posicional
dicion= dict()	            dicionario{}	    imutavel    chave:valor


DICIONARIOS

Conjunto nao-ordenado de pares chave:valor.
Contem lista de pares chave:valor, separados por virgulas.
São delimitados por {}, indicando relação chave:valor.
As chaves são imutáveis.

1. Dicionários Simples:

a) Declarando dicionário

Delimitando por chaves {} ou pela classe DICT.'''

pessoa = dict(nome = 'Guilherme', idade = 28)
pessoa = {'nome': 'Guilherme', 'idade': 28}

'''Agrupando Dicionarios dentro de uma Lista:'''

estados = []
estado1 = {'uf': 'São Paulo', 'sigla':'SP'}
estado2 = {'uf': 'Paraná', 'sigla':'PR'}
estados.append(estado1)                     # chave:'estado1' / valor: {'uf': 'São Paulo', 'sigla': 'SP'}
estados.append(estado2)                     # chave:'estado2' / valor: {'uf': 'Paraná', 'sigla': 'PR'}

#estados = [{'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Paraná', 'sigla': 'PR'}]

print(estado1) #pela chave                  # {'uf': 'São Paulo', 'sigla': 'SP'}
print(estado2) #pela chave                  # {'uf': 'Paraná', 'sigla': 'PR'}
print(estados[1]) #pela posição na lista    # {'uf': 'Paraná', 'sigla': 'PR'}

'''
b) Edição
Se o dado não existir, adiciona chave e valor.
Se o dado já existir, sobrescreve.'''

pessoa['telefone'] ='3333-1234'
pessoa['nome'] = "Alessandra"

'''
c) Acesso ao dado: é posicional [chave]'''

print(pessoa['nome'])      # Alessandra
print(pessoa['idade'])     # 28
print(pessoa['telefone'])  # 3333-1234

print(pessoa) #{'nome': 'Alessandra', 'idade': 28, 'telefone': '3333-1234'}
print()

'''Dicionario dentro de Lista: precisa da posição do elemento/e a chave do dado'''

print(estados)              # [{'uf': 'São Paulo', 'sigla': 'SP'}, {'uf': 'Paraná', 'sigla': 'PR'}]
print(estados[1])           # {'uf': 'Paraná', 'sigla': 'PR'}
print(estados[0]['sigla'])  # SP
print()


'''
2. Dicionarios Aninhados

Podem armazenar qualquer tipo de objeto como valor.
A chave para o objeto deve ser imutável.'''

contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'},
    'alessandra@gmail.com': {'nome': 'Alessandra', 'idade': 36, 'telefone': '3333-1000', 'senhas': {'netflix': '0101', 'apple': '0202'}},
    'giovana@gmail.com': {'nome': 'Giovana', 'idade': 24, 'telefone': '3300-1000', 'apelido': 'Lioness'},
}

print(contatos ['alessandra@gmail.com'] ['senhas'])
print(contatos ['alessandra@gmail.com'] ['senhas'] ['apple'])
print()


# 3. Iterando dicionários

print(contatos.keys(),'\n')          # chaves (nome, idade, telefone)
print(contatos.values(),'\n')        # valores 
print(contatos.items(),'\n')         # chave:valor

for chave, valor in contatos.items():
    print(chave, valor)
print()

for chave in contatos.keys():
    print(chave)
print()

for valor in contatos.values():
    print(valor)
print()    