'''Biblioteca urllib

A biblioteca urllib é uma biblioteca padrão do Python usada para trabalhar com URLs.

1. O que você pode fazer com urllib:

Tarefa	                        Módulo/método usado	                    Descrição

Acessar conteúdo da web	        urllib.request.urlopen()	            Faz requisições HTTP para abrir páginas ou arquivos
Trabalhar com cookies	        urllib.request.HTTPCookieProcessor()	Armazena e envia cookies automaticamente
Codificar parâmetros para URL	urllib.parse.urlencode()	            Constrói URLs com parâmetros de forma segura
Analisar URLs	                urllib.parse.urlparse()	                Separa partes da URL:protocolo, domínio, caminho, etc.
Lidar com erros de rede	        urllib.error.URLError, HTTPError	    Trata falhas ao acessar páginas (ex: 404, 500 etc.)

2. Estrutura básica do urllib: é dividida em submódulos.

- urllib.request: Abrir e ler URLs.
- urllib.parse: Analisar e montar URLs.
- urllib.error: Lidar com erros HTTP.

Dica:
- Em muitos casos, bibliotecas como requests são mais simples e modernas que urllib.
- urllib continua muito usada quando se deseja evitar bibliotecas externas.
'''

# Exemplo 1 - Acessar o conteúdo de uma página

from urllib.request import urlopen

url = "http://example.com"
resposta = urlopen(url)
html = resposta.read().decode('utf-8')

print(html)


# Exemplo 2 - Construir uma URL com parâmetros

from urllib.parse import urlencode

parametros = {'q': 'python urllib', 'lang': 'pt'}
url = "https://www.google.com/search?" + urlencode(parametros)
print(url)


# Exemplo 3 - Aplicação com interação do usuario

from urllib.request import urlopen
from urllib.error import URLError

try:
    site = urlopen('http://www.checktudo.com.br')
except URLError:
    print('O site está indisponível no momento.')
else:
    print('Site disponível.')