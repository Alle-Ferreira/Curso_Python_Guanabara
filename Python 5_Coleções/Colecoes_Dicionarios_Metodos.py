# DICIONARIOS: Metodos da classe Dict

# 1.1. Metodos de Dicionarios

contato = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'},
    'alessandra@gmail.com': {'nome': 'Alessandra', 'idade': 36, 'telefone': '3333-1000', 'senhas': {'netflix': '0101', 'apple': '0202'}},
    'giovana@gmail.com': {'nome': 'Giovana', 'idade': 24, 'telefone': '3300-1000', 'apelido': 'Lioness'},
}

# a) .copy()

contatos = contato.copy()           # copia o dicionario inteiro.

brasil = list()                     # aceita .append()
estados = dict()                    # não aceita .append(), pois é posicional.
for estado in range (3):
    estados['uf'] = input('UF:')
    estados['sigla'] = input('Sigla:')
    brasil.append(estado.copy())    # criar um copia do dicionario, e dps adiciona na lista


# b) fromkeys ([])
# cria as chaves do dicionario, que podem ser criadas sem valor.

print(contato.fromkeys(['cidade', 'cep']))
print(contato.fromkeys(['uf'], 'df'))
print()


# .keys
# retorna quais são as chaves do dicionario.

print(contato.keys())
print()


# .get
# uma das formas de acessar chaves e/ou valores do dicionario.

print(contato.get('senhas'))   # se não achar a chave solicitada, trará NONE.
print(contato.get('uf', {}))   # se não achar a chave solicitada, trará todas as chaves e valores.
print(contato.get('giovana@gmail.com', {})) 
print()


# .items
# Retorna uma lista de tuplas.
# Muito util ao usar comando FOR, para iterar itens do dicionario.

print(contato.items())
print()


# .setdefault
# atribui valor e chaves, com verificação prévia de existencia.
# não atribui valor se outro valor já existir, para a chave especificada.

contato.setdefault('nome', 'Guilherme')


# .update


