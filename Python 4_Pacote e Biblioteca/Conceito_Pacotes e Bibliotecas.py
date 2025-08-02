'''Bibliotecas - Pacotes Python:

I - Pacotes Nativos: não precisam instalar, podem ser importados diretamente.

1. Math         calculos matematicos simples.
2. Random
3. Tkinter      usado para desenvolver interfaces gráficas.
4. Smtplib      usado para permitir envio de e-mails.
5. Datetime

II - Pacotes Externos: nao vem instalado no Python, então primeiro precisa instalar.

Nome módulo	    Pra que serve

numpy	        Cálculos, operações matemáticas e simulações.
pandas	        Manipulaçao de dados
scikit-learn	Modelos de aprendizado de máquina
matplotlib	    Visualização de dados
requests	    Biblioteca de comandos de comunicação pelo protocolo HTTP
flask	        Construção de aplicações web
emoji           Emojis 
'''
'''
1. Math:

O math é amplamente utilizado devido à sua eficiência e facilidade de uso para operações matemáticas comuns, entretanto, ele não suporta operações com números complexos. 
As funções no módulo math são projetadas para trabalhar exclusivamente com números reais (float e int). 
Se você tentar passar um número complexo para uma função do módulo math, ele retornará um erro. 

.ceil(): arredonda numero para cima
.floor(): arredonda numero para baixo
.trunc(): exclui casas decimais             # truncate 
.pow (): calcula a potencia                 # power
.sqrt(): calcula raiz quadrada              # square root
.factorial(): calculo de fatoriais
.cos(x): cosseno de x
.sin(x): seno de x
.log(x, b): logaritmo de x na base b
.pi: valor de Pi (3.141592...)
.e: valor de e (2.718281...)

Sintaxe de Importação:

a) Importando toda a biblioteca: precisa referenciar a biblioteca no codigo.     
'''
import math    
         
numero = int(input('Informe um numero: '))
raiz_quadrada = math.sqrt(numero)
print(raiz_quadrada)
print()

'''
b)  Importando classe(s) específicas da biblioteca: não precisa referenciar.
'''
from math import sqrt, trunc    

numero = int(input('Informe outro numero: '))
raiz_quadrada = sqrt(numero)
print(trunc(raiz_quadrada))
print()


'''
2. Random:

.random(): numero randomico de ponto flutuante no intervalo (00,0, 1,0)
.randint(): numero randomico inteiro, dentro do intervalo definido.
.randrange(): gera um número inteiro aleatório a partir de uma intervalo específico.
              aceita start, stop e step.
.uniform(a, b): número de ponto flutuante N tal que a ≤ N ≤ b
.gauss(mu, sigma): distribuição gaussiana. mu é a média e sigma é o desvio padrão.
.normalvariate(mu, sigma): distribuição gaussiana. mu é a média e sigma é o desvio padrão.
.choice(seq): elemento aleatório de uma sequência não vazia seq.
.shuffle(x[, random]): embaralha a sequência x no lugar.
.sample(pop, k): uma sequência de tamanho k de elementos escolhidos da população pop, sem repetição. 
                 usada para amostragem sem substituição.
'''
import random

numero = random.random()
print(numero)
print()

numero1 = random.randint(1, 50)   # numero entre o 1 na posição (0) e o 50 posição (49).
print(numero1)
print()

numero2 = random.randrange(1,150,2)  # numero entre posição 1 (0) à posição 150 (149), pulando de 2 em 2 numeros.
print(numero2)
print()


'''
3. smtplib
Usado para permitir envio de e-mails.'''

#import dos pacotes necessários
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#criação de um objeto de mensagem
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU E-MAIL"
msg['To'] = "E-MAIL DESTINO"
msg['Subject'] = "ASSUNTO"

#criação do corpo da mensagem
msg.attach(MIMEText(texto, 'plain'))

#criação do servidor
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')

