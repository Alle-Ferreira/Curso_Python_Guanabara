arquivo = 'nome_arquivo'

'1. Abrir e ler: rt'
teste = open(arquivo, 'rt')        # rt: read text

arquivo.readline()      # O método .readline() lê apenas a primeira linha do arquivo.
arquivo.readlines()     # O método .readlines() lê todas as linhas do arquivo.
arquivo.read()          # O método .readlines() lê todas as linhas do arquivo.


'2. Edita e criar arquivo, caso na exista: wt+'
teste = open(arquivo, 'wt+')   


'3. Fechar'
teste.close()


'4. Funções Úteis de Manipulação de Arquivos'

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

def ler_arq_txt(nome_arq, título):                  #usa a função formatar_titulos

    try:
        arquivo = open(nome_arq, 'rt')              #rt: read text
    except:
        print('Erro na leitura do arquivo.')
    else:
#       formatar_titulos(título)
        print(arquivo.read())
    finally:
        arquivo.close()

def ler_arq_txt_formatado(nome_arq, título):        #usa a função formatar_titulos 
    try:
        arquivo = open(nome_arq, 'rt')               #rt: read text
    except:
        print('Erro na leitura do arquivo.')
    else:
        formatar_titulos(título)
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')          #retira espaçamento(\n) incluido p/def_cadastrar() em cada registro.
            print(f'{dado[0]:<25} {dado[1]:>3} anos')   #dado[0] = nome, e dado[1] = idade
    finally:
        arquivo.close()