'''
Sistema interativo de ajuda em Python'''

def mostrar_titulo(mensagem, cor='\033[m'):
    """Exibe um título com destaque visual."""
    tamanho = len(mensagem) + 4
    print(cor + '-' * tamanho)
    print(f'  {mensagem}')
    print('-' * tamanho + '\033[m')


def sistema_ajuda(nome_comando):
    """Acessa o help do Python e mostra com visual organizado."""
    mostrar_titulo(f"Acessando o manual do comando '{nome_comando}'", '\033[44m')  # fundo azul
    print('\033[33m')  # cor amarela para destacar
    help(nome_comando)
    print('\033[m')  # reset


def help_me():
    """Loop principal do sistema de ajuda interativo.
    Mini-sistema que utilize o Interactive Help do Python. 
    O usuário vai digitar o comando e o manual vai aparecer. 
    Quando o usuário digitar a palavra 'FIM', o programa se encerrará."""
    while True:
        mostrar_titulo('SISTEMA DE AJUDA PyHELP', '\033[42m')  # fundo verde
        comando = input('\033[1;34mFunção ou biblioteca > \033[m')  # azul negrito

        if comando.strip().upper() == 'FIM':
            mostrar_titulo('ATÉ LOGO!', '\033[41m')  # fundo vermelho
            break
        elif comando.strip() == '':
            continue  # ignora entradas vazias
        else:
            sistema_ajuda(comando.strip())


'''
# Main Program
help_me()
'''