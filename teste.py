cores = {                                   # Variável Global: declarar fora da função
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

def ler_int_cor(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError):
            print(f"{cores['vermelho']}Por favor, digite um número inteiro válido.{cores['padrao']}")
        except KeyboardInterrupt:
            print(f"\n{cores['vermelho']}Erro: entrada de dados interrompida pelo usuário.{cores['padrao']}")
            return 0

def criar_menu(titulo, conteudo, maior_opcao, cor="padrao"):
    '''
    # Chama a função "ler_int_cor"
    # Exibe um menu colorido com validação de entrada. Parâmetros:
        - titulo (str): título do menu
        - maior_opcao (int): maior número de opção aceitável
        - cor (str): chave da cor no dicionário 'cores'
        - conteudo (str): opções numericas do menu, formatadas linha a linha. Exemplo:
            [1] Cadastrar Pessoa
            [2] Listar Pessoas
            [0] Sair do Sistema 
        '''
    tamanho = len(titulo) + 15
    print(cores[cor], end='')
    print('-' * tamanho)
    print(f'{titulo.center(tamanho)}')
    print('-' * tamanho)
    print(conteudo)
    print('-' * tamanho)
    print(cores['padrao'], end='')
    entrada = ler_int_cor('Digite o número da opção desejada: ')
    while entrada < 0 or entrada > maior_opcao:
        entrada = ler_int_cor("Opção inválida, tente novamente: ")
    return entrada

def ler_resposta(entrada):
    while True:
        resposta = input(entrada).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print('Erro: digite apenas S ou N.')
# Main Program

conteudo = (''' 
[1] Cadastrar Pessoa
[2] Listar Pessoas
[0] Sair do Sistema
''')
entrada = criar_menu('Menu do Sistema', conteudo, 2, 'amarelo')

pessoas = []
while True:
    if entrada == 1:
        pessoas['nome'] = input('Informe nome completo, da pessoa a ser cadastrada: ')
        pessoas['idade'] = ler_int_cor(f'Informe a idade desta pessoa: ')
    elif entrada == 2:
        for chave, valor in pessoas.items():
            print(chave, valor)
    else: 
        print('Sistema Encerrado. Até logo!')





