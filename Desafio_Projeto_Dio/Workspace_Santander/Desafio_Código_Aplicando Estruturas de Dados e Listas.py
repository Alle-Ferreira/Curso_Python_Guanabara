'''
DESAFIO 1 
Descrição
Crie um sistema de carrinho de compras que permita adicionar produtos e calcular o valor total da compra.

Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).
Saída
Lista dos produtos adicionados e o total da compra.
Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	                        Saída
2                           Pão: R$3.50
Pão 3.50                    Leite: R$4.00
Leite 4.00	                Total: R$7.50

3                           Arroz: R$2.50
Arroz 2.50                  Brigadeiro: R$3.00
Brigadeiro 3.00             Sorvete: R$14.50
Sorvete 14.50	            Total: R$20.00

3                           Maçã: R$2.00
Maçã 2.00                   Pera: R$3.50
Pera 3.50                   Biscoito: R$5.50
Biscoito 5.50	            Total: R$11.00

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.'''

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for produto in range(n):
    linha = input().strip()          
    posicao_espaco = linha.rfind(" ")           # Encontra última ocorrência espaço: separa nome e preço
    item = linha[:posicao_espaco]               # Separa o nome do produto e o preço
    preco = float(linha[posicao_espaco + 1:])   # Separa o nome do produto e o preço
    carrinho.append((item, preco))              # Adiciona ao carrinho
    total += preco

# TODO: Exiba os itens e o total da compra
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")
print(f'Total: R${total:.2f}')

'''
DESAFIO 2

Descrição
Uma empresa quer criar um organizador de eventos que divida os participantes em grupos de acordo com o tema escolhido.

Entrada: Lista de participantes e o tema escolhido por cada um.
Saída: Dicionário agrupando os participantes por tema.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
'''

# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Loop para armazenar participantes e seus temas
for participante in range(n):
    linha = input().strip()
    nome, tema = linha.split(",")  # Divide em duas partes usando vírgula como separador
    nome = nome.strip()
    tema = tema.strip()
    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")