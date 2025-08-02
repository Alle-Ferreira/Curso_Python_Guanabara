''' 
Módulo Datetime: manipulação de dados

4. Classe datetime.timedelta()
Adiciona intervalos de tempo
Todos os argumentos são opcionais e o padrão é 0. 
Os argumentos podem ser números inteiros ou ponto flutuantes, positivos ou negativos.
Apenas days, seconds e microseconds são armazenados internamente. 

Os argumentos são convertidos para essas unidades:
Um milissegundo é convertido em 1000 microssegundos.
Um minuto é convertido em 60 segundos.
Uma hora é convertida em 3600 segundos.
Uma semana é convertida para 7 dias.

Dias, segundos e microssegundos são normalizados para que a representação seja única:
0 <= microseconds < 1000000
0 <= seconds < 3600*24 (o número de segundos em um dia)
-999999999 <= days <= 999999999

Operações suportadas:
https://docs.python.org/pt-br/3.13/library/datetime.html#timedelta-objects

'''
# Exemplo Sintaxe 1:
from datetime import datetime, timedelta

tempo_carro_p = timedelta(minutes=30)
tempo_carro_m = timedelta(minutes=45)
tempo_carro_g = timedelta(minutes=60)
data_atual = datetime.now()

tempo_entrega_p = data_atual + tempo_carro_p
tempo_entrega_m = data_atual + tempo_carro_m
tempo_entrega_g = data_atual + tempo_carro_g

tipo_carro = input('Qual o tamanho (p, m, g) do veículo? ')        # Importante: 'P' e 'p' sao diferentes

print(f'A entrega do veículo ocorreu em {data_atual}.')

if tipo_carro == 'p':
    print(f'Seu veículo estará pronto em {tempo_entrega_p}.')
elif tipo_carro == 'm':
    print(f'Seu veículo estará pronto em {tempo_entrega_m}.')
else:
    print(f'Seu veículo estará pronto em {tempo_entrega_g}.')
print()


# Exemplo Sintaxe 2:
import datetime

dt_abertura = datetime.datetime(2025, 5, 20, 12, 0)                    # 1o momento
dt_update = dt_abertura + datetime.timedelta(weeks=1, hours=12)        # 2o momento
prazo_inscricoes = dt_update + datetime.timedelta(days=3, hours=12)    # 3o momento

print(f'O evento terá inicio em {dt_abertura}')
print(f'A primeira atualização ocorrerá no dia {dt_update}')
print(f'Apos a atualização, os candidatos terão até {prazo_inscricoes} para realizar sua inscrição.')
print()


# Exemplo 3:
from datetime import date, timedelta

print(date.today() - timedelta(days=1))
print(date.today() + timedelta(days=-3))
print()


'''
Importante: a Classe .timedelta() não suporta o objeto .time()
Exemplos de como contornar, para trabalhar apenas com exibição da hora ou data.
''' 
from datetime import  datetime, timedelta

# Sintaxe 1: especificando a hora, sem os milesimos de segundos, exibirá o msm formato
hora_evento = datetime(2025, 5, 20, 13, 26) - timedelta(hours=3)
print(hora_evento.time()) 
print()

# Sintaxe 2: usando .today(), exibirá o formato padrão, com milesimos de segundos.
hora_evento = datetime.today() - timedelta(hours=3)
print(hora_evento.time())                               # Exibindo somente a hora
print(hora_evento.date())                               # Exibindo somente a data
print()
