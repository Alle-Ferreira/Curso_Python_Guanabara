''' Tipos Sequenciais e Dicionarios

Em Python, os tipos sequenciais, como listas, tuplas e conjuntos, têm um papel essencial na organização e manipulação de dados.
Permitem armazenar coleções ordenadas e únicas de elementos. 
Operadores comuns, como indexação, fatiamento e concatenação, são utilizados para acessar e manipular essas sequências de forma eficiente.

Além disso, os dicionários de estruturas de dados chave-valor oferecem uma maneira eficaz de associar informações.
São úteis para armazenamento e recuperação de dados de forma rápida e eficiente em aplicações Python.


1. Tipos Sequenciais

- Listas: sequências mutáveis, normalmente usadas para armazenar coleções de itens homogêneos.
- Tuplas: sequências imutáveis, tipicamente usadas para armazenar coleções de itens heterogêneos.
- Objetos RANGE: sequência imutável de números, frequentemente usado em loops com número específico de vezes.
- Objetos STR (strings): possível armazenar letras, números, espaços, pontuação e diversos símbolos.

A indexação dos itens é iniciada com 0 e cada item tem o seu índice incrementado a uma unidade em relação ao item anterior. 
Python também permite a indexação com valores negativos: o valor -1 é o índice do último item, e cada item anterior é decrementado de uma unidade em relação ao sucessor.


2. Operadores Sequenciais Comuns:

Permitem a manipulação dos tipos sequenciais, inclusive as strings. 
Vale ressaltar a sobrecarga dos operadores + e *, que realizam operações diferentes quando os operandos são numéricos ou sequenciais.

Uso	            Resultado

x in s	        True se x for um subconjunto de s
x not in s	    False se x for um subconjunto de s
s + t	        Concatenação de s e t
n*s	            Concatenação de n cópias de s
s[i]	        Caractere de índice i em s
len(s)	        Comprimento de s
min(s)	        Menor item de s
max(s)	        Maior item de s

Importante: use o utilitário help no Python Console para verificar a lista completa. 
Para isso, basta digitar help(str) e pressionar [ENTER] no teclado.


3. Dicionários:

Permitem que itens de uma sequência recebam índices definidos pelo usuário. 
Um dicionário contém pares de (chave, valor). 

a) Estrutura geral de um objeto dicionário:

{<chave 1>:<valor 1>, <chave 2>:<valor 2>, ..., <chave i>:<valor i>}

pessoas = {'111222335-44':['João','Silva'], '222333444-55':['Maria', 'Santos'], '353444555-66':
['Jorge', 'Silva']} 


b) Acessando o dicionario pelo CPF:

pessoas ['111222353-44']      retorna     ['João', 'Silva']
'''