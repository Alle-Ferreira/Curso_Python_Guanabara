def formatar_titulos(titulo, cor='padrao'):
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
    tamanho = len(titulo) + 20
    print(cores[cor], end='')
    print('-' * (tamanho))
    print(f'{titulo.center(tamanho)}')
    print('-' * (tamanho))
    print(cores['padrao'], end='')
    

class Extrato:

    def __init__(self):
        self.transacoes = []

    def exibir_extrato(self, conta):
            formatar_titulos(f'Extrato da Conta {conta}', 'azul')
            for transacao in self.transacoes:
                print(f'{transacao[0]:15} R$ {transacao[1]:10.2f} {transacao[2]: %d/%m/%Y}')
            print()


