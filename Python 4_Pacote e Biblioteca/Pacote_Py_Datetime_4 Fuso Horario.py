
'''
5. Método datetime.timezone()

Objetos da classe .timezone():

timezone.utc()              O fuso horário UTC, timezone(timedelta(0)).
timezone.utcoffset()        Diferença seu fuso horario x UTC
timezone.tzname()
timezone.dst()
timezone.fromutc()

Aviso: 
Como objetos datetime ingênuos são tratados por muitos métodos datetime como hora local, 
é preferível usar datetimes conscientes para representar horas em UTC. 
A maneira recomendada para criar um objeto representando a hora local em UTC é chamando datetime.now(timezone.utc).
'''

from datetime import timezone, datetime, timedelta

# 5.1. Objeto ingênuo (sem fuso horário):
data = datetime.now(timezone.utc)
print(data)
print()


# 5.2. Objeto consciente (com fuso horário):
agora = datetime.now().astimezone(timezone.utc)
print(agora)
print()


# 5.3. Usando .timedelta() para compensar fusos horários manualmente:

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sampa = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data_sampa)
print()


'''
6. Método datetime.tzinfo:

tzinfo.tzname(dt)
Retorna o nome do fuso horário correspondente ao objeto datetime dt, como uma string
'''


'''
7. Biblioteca zoneinfo:

Padrão Python a partir da versão 3.9
- Nomes de fuso do banco de dados IANA ("America/New_York", "Europe/London")
- Objeto ZoneInfo difere da classe zoneinfo pelas letras maiúsculas
'''

from datetime import datetime
from zoneinfo import ZoneInfo     


# 7.1. Definindo o fuso horario (UTC)

agora_sp = datetime.now(ZoneInfo("America/Sao_Paulo"))
print(agora_sp)


# 7.2. Convertendo para determinado fuso horario (UTC)

agora_utc = datetime.now(timezone.utc)               # Data e hora em UTC

agora_sp = agora_utc.astimezone(ZoneInfo("America/Sao_Paulo"))
print(agora_sp)


# 7.3. Nomes dos fusos horários:

# import zoneinfo

#print(sorted(zoneinfo.available_timezones()))       # lista os nomes das timezones.
print()


