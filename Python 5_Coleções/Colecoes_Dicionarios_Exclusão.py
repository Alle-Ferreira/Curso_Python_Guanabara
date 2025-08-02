# DICIONARIOS: Metodos da classe Dict

# 1.2. Metodos de Exclusão em Dicionarios


contatos = {
    'guilherme@gmail.com': {'nome': 'Guilherme', 'idade': 28, 'telefone': '3333-1234'},
    'alessandra@gmail.com': {'nome': 'Alessandra', 'idade': 36, 'telefone': '3333-1000', 'senhas': {'netflix': '0101', 'apple': '0202'}},
    'giovana@gmail.com': {'nome': 'Giovana', 'idade': 24, 'telefone': '3300-1000', 'apelido': 'Lioness'},
}


# .pop
# remove items do dicionario
# se não encontrar a chave, ele dará erro, a menos que receba uma 2a orientação.

print(contatos.pop('alessandra@gmail.com'))
print(contatos.keys())
print()

print(contatos.pop('alessandra@gmail.com', 'não encontrado'))
print()


# .popitem
# apaga todos os items, um a um.

contatos.popitem()   
print(contatos)
print()


# .clear()
# apaga o dicionario inteiro.

contatos.clear()  