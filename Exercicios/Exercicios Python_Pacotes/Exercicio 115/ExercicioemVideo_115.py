'''
Desafio Final: Exercício Python 115
Menu usando modularização

Crie um pequeno sistema de modularização, em um arquivo de texto simples:
    - Atributos: nome e idade
    - Funcionalidades: cadastrar e listar pessoas.

Etapas:
    115.a) Criar um menu em Python: 
        - Incluir título, cores e barras de separação para o menu de opções.
        - Incluir opção para "Sair do sistema".
        - Validar entradas.
    115.b) Arquivos com Python: acesso a arquivos usando o Python.
        - Incluir armazenamento de dados em arquivo de texto simples.
    115.c) Manipulação de Arquivos
    '''

# Main Program

from pacote_exercicio115 import *
cores = {     # Variável Global, declarada fora das funções.
    'padrao': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'negrito': '\033[1m',
    'fundo_azul': '\033[44m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
}

nome_arquivo = 'dados_pessoas.txt'  #arquivo precisa estar no mesmo diretorio do projeto.
conteudo = ('[1] Cadastrar Pessoa', '[2] Listar Pessoas', '[3] Importar Cadastro', '[0] Sair do Sistema')

while True:
    criar_menu('SISTEMA DE CADASTRO', conteudo, 'verde')
    entrada = ler_int_cor('Digite o número da opção desejada: ')
    if entrada == 0: 
        print(f'{cores["amarelo"]}Sistema Encerrado. Até logo!{cores["padrao"]}\n')
        break
    elif entrada == 1:
        while True:
            formatar_titulos('INCLUSÃO DE NOVO CADASTRO', 'azul')
            nome = input('Informe nome completo: ')
            idade = ler_int_cor('Informe a idade desta pessoa: ')
            cadastrar(nome_arquivo, nome, idade)
            resposta = ler_resposta(f'{cores["amarelo"]}Deseja cadastrar outra pessoa? S/N: {cores["padrao"]}')
            if resposta == 'N':
                break
    elif entrada == 2:
        ler_arq_txt(nome_arquivo,'PESSOAS CADASTRADAS')
    elif entrada == 3:
        if not testar_arq_txt(nome_arquivo):
            criar_arq_txt(nome_arquivo)
        ler_arq_txt(nome_arquivo,'PESSOAS CADASTRADAS')
    else:
        print('Opção inválida, tente novamente: ')

