'''II - Formatação de Textos: cores e fontes'''

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

'''
1. Formatação de Títulos:(Acessando o Dicionario "cores", fora da função)

* Usa lista de cores da variavel global
'''
def formatar_titulos(titulo, cor='padrao'):
    tamanho = len(titulo) + 15
    print(cores[cor], end='')
    print('-' * (tamanho))
    print(f'{titulo.center(tamanho)}')
    print('-' * (tamanho))
    print(cores['padrao'], end='')


'''
2. Criando Menus com titulo e cor:
'''

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


'''
3. Colorindo o Texto: (Acessando "cores" dentro da função, com GET)

Exemplo 1: usa o menu de cores como variavel global
'''
def print_colorido(mensagem, cor='padrao'):
    inicio = cores.get(cor, '\033[0m')
    fim = '\033[0m'
    print(f"{inicio}{mensagem}{fim}")


print_colorido('Erro: número inválido.', 'vermelho')
print_colorido('Sucesso! Dados salvos.', 'verde')
print_colorido('Atenção! Campo obrigatório.', 'amarelo')


'''
Exemplo 2: insere o menu de cores na função
'''
def cor_texto(texto, cor="padrao"):
    cores = {
        "vermelho": "\033[31m",
        "verde": "\033[32m",
        "amarelo": "\033[33m",
        "azul": "\033[34m",
        "padrao": "\033[0m"
    }
    return f"{cores.get(cor, cores['padrao'])}{texto}\033[0m"


print(cor_texto("Erro: valor inválido!", "vermelho"))
print(cor_texto("Tudo certo!", "verde"))
print(cor_texto("Aviso: verifique os dados", "amarelo"))
print(cor_texto("Bem-vindo!", "azul"))

