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

def formatar_titulos(titulo, cor='padrao'):
    tamanho = len(titulo) + 15
    print(cores[cor], end='')
    print('-' * (tamanho))
    print(f'{titulo.center(tamanho)}')
    print('-' * (tamanho))
    print(cores['padrao'], end='')

def criar_menu(titulo, conteudo, cor="padrao"):
    '''
    # Chama a função "ler_int_cor"
    # Exibe um menu colorido com validação de entrada. Parâmetros:
        - titulo (str): título do menu
        - maior_opcao (int): maior número de opção aceitável
        - cor (str): chave da cor no dicionário 'cores'
        - conteudo (str): opções numericas do menu, formatadas linha a linha.
        '''
    tamanho = len(titulo) + 15

    print(cores[cor], end='')
    print('-' * tamanho)
    print(f'{titulo.center(tamanho)}')
    print('-' * tamanho)

    for item in conteudo:
        print(item)
    print('-' * tamanho)
    print(cores['padrao'], end='')

def cadastrar(nome_arquivo, nome='desconhecido', idade=0):
    try:
        arquivo = open(nome_arquivo, 'at')
    except:
        print ('Arquivo nao encontrado')
    else:
        try:
            arquivo.write(f'{nome}; {idade}\n')
        except:
            print('Houve um erro ao salvar o arquivo.')
        else:
            print(f'Cadastro {nome} criado com sucesso!')
            arquivo.close()

def ler_int_cor(entrada):
    while True:
        try:
            return int(input(entrada))
        except (ValueError, TypeError):
            print(f'{cores["vermelho"]}Por favor, digite um número inteiro válido.{cores["padrao"]}')
        except KeyboardInterrupt:
            print(f'\n{cores["vermelho"]}Erro: entrada de dados interrompida pelo usuário.{cores["padrao"]}')
            return 0

def ler_resposta(entrada):
    while True:
        resposta = input(entrada).strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print(f'\n{cores["vermelho"]}Erro: digite apenas S ou N.{cores["padrao"]}')

def testar_arq_txt(nome_arquivo):
    try:
        teste = open(nome_arquivo, 'rt')        # rt: read text
        teste.close()
    except FileNotFoundError:
        print('arquivo nao encontrado')
        return False
    else:
        print('arquivo encontrado')
        return True

def criar_arq_txt(nome_arquivo):
    try:
        teste = open(nome_arquivo, 'wt+')       
        # wt+: write text, '+' add se não existir o arq.
        teste.close()
    except:
        print('Ocorreu um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso.')

def ler_arq_txt(nome_arq, título):              #usa a função formatar_titulos 
    try:
        arquivo = open(nome_arq, 'rt')          #rt: read text
    except:
        print('Erro na leitura do arquivo.')
    else:
        formatar_titulos(título)
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')              #retira espaçamento '\n', incluido p/função cadastrar() no final de cada registro.
            print(f'{dado[0]:<25} {dado[1]:>3} anos')      #dado[0] = nome, e dado[1] = idade
    finally:
        arquivo.close()

