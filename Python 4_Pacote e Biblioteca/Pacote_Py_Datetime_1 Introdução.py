''' Introdução ao módulo Datetime

Nativo do python: em instalado, precisa apenas importar.

Classes: principais classes úteis

1.date():                            aa/mm/dd 
2.time():                            00:00:00
3.datetime():                        aa/mm/dd 00:00:00
4.timedelta
5.timezone()
6.tzinfo()
7.zoneinfo()

b) Constantes:
MINYEAR: o menor número de ano permitido no objeto date. ou datetime.MAXYEAR é 1
MAXYEAR: o maior número de ano permitido no objeto date. ou datetime.MAXYEAR é 9999
UTC: Apelido para o singleton de fuso horário UTC datetime.timezone.utc.

ano: MINYEAR <= year <= MAXYEAR
mes: 1 <= month <= 12
dia: 1 <= day <= numero de dias do mes e ano fornecidos

hour: 0 <= hour < 24
minute: 0 <= minute < 60
second: 0 <= second < 60
microsecond: 0 <= microsecond < 1000000
fold in [0, 1]

Atributos não obrigatórios, na ausencia de argumento serão:
hour=0
minute=0 
second=0
microsecond=0
tzinfo=none
fold=0
'''

''' 
1. Classe datetime.date()
Atributos: year, month e day.
'''

# Sintaxe 1:
import datetime

data = datetime.date(2023, 7, 19)     
print(data)
print(1)

# Sintaxe 2:
from datetime import date             # Importa classe .date, do módulo datetime

data = date(2023, 7, 19)
print(data)

'''1.1. Objeto date.today()
Atributos: data(year, month e day)
date.today(): data atual
'''
dia_local = date.today()
print(dia_local)

print(date.today())             # retorna data atual.


'''
2. Classe datetime.time()
- Atributos: hour, minute, second, microsecond e tzinfo.

- Retorna a hora atual, sujeito a ajustes por meio do objeto tzinfo.
- Presume que todos os dias tenham exatamente 24*60*60 segundos. 
- Não há noção de “segundos bissextos” aqui.

time()	Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 00:00:00 do dia 1 de janeiro de 1970.

ctime(segundos)	Uma string representando o horário local, calculado a partir do número de segundos passado como parâmetro.
gmtime(segundos)	Converte o número de segundos em um objeto struct_time descrito a seguir.
localtime(segundos)	Semelhante à gmtime(), mas converte para o horário local.
sleep(segundos)	A função suspende a execução por determinado número de segundos.

time.min: o time mais cedo que pode ser representado como time(0, 0, 0, 0).
time.max: o time mais tardio que pode ser representado como time(23, 59, 59, 999999).
time.resolution: A menor diferença possível entre objetos time diferentes, timedelta(microseconds=1).
time.tzinfo: objeto do argumento tzinfo para o construtor da classe time (None qdo sem argumento).
'''

# Sintaxe 1
from datetime import time     # Importa classe .time, do módulo datetime

hora = time(12, 21, 0)
print(hora)
print()

# Sintaxe 2
import time

x = time.time()
print(f'Local time: {time.ctime(x)}')

'''
Índice	Atributo	Valores
0	    tm_year	    Por exemplo, 2020
1	    tm_mon	    range [1, 12]
2	    tm_mday	    range [1, 31]
3	    tm_hour	    range [0, 23]
4	    tm_min	    range [0, 59]
5	    tm_sec	    range [0, 61]
6	    tm_wday	    range [0, 6] Segunda-feira é 0
7	    tm_yday	    range [1, 366]
8	    tm_isdst	0,1 ou -1
N/A	    tm_zone	    Abreviação do nome da timezone
'''