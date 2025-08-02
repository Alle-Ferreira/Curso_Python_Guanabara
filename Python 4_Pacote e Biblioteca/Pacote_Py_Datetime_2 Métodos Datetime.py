''' Pacote Datetime - Metodo Datetime
 
3. Classe datime.datetime()
Atributos obrigatórios: year, month, day
Atributos não obrigatórios: hour, minute, second, microsecond,  tzinfo, fold
Possui vários objetos:

3.1. now()
3.2. today()
3.3. utcnow()
'''

from datetime import datetime   # Importa classe .datime, do módulo datetime

acesso = datetime(2023, 7, 19, 10, 30, 20)
print(acesso)
print()


''' 
3.1. Objeto .datetime.now()
Retorna data/horario atuais, em função da tzinfo da máquina.
Atributos: data(year, month e day), horario(hour, minute, second, microsecond), e tzinfo.
'''

from datetime import datetime

print(datetime.now())
print()


'''
3.2. Objeto datetime.today() / 
Retorna data /e horario atuais.
Atributos: data(year, month e day), horario(hour, minute, second, microsecond), e tzinfo.

datetime.today(): data e horario atuais
'''

from datetime import date, datetime  # Importa classes .date e .datime, do módulo datetime

# Sintaxe 1
horario_local = datetime.today()
print(horario_local)

# Sintaxe 2
print(datetime.today())         # retorna data e horario atuais.
print()

'''
2.3. Objeto datetime.utcnow()
Retorna a data e hora atual em UTC, com tzinfo como None.
Este é similar a datetime.now(), mas retorna a data e hora atual em UTC, como um objeto datetime ingênuo.
'''
# Descontinuado desde a versão 3.12: Use datetime.now() com UTC.


'''
Formatação e Conversão
https://docs.python.org/pt-br/3.13/library/datetime.html#strftime-and-strptime-behavior

5. Objeto datetime.strftime()
Formata a string para exibição, de acordo com a mascara especificada.
Podemos exibir apenas parte dos atributos da string:

%a dia da semana
%d dia
%m mes formato numerico
%M minutos
%y ano aa
%Y ano aaaa
%h mes por extenso
%H hora
'''

from datetime import datetime

horario_local = datetime.now()
print(horario_local)

print(horario_local.strftime('%d/%m/%Y %H:%M'))         # dd/mm/aaaa 00:00
print(horario_local.strftime('%d/%m/%y %H:%M'))         # dd/mm/aa 00:00
print(horario_local.strftime('%d/%m/%y %a'))            # dd/mm/aa weekday
print(7.1)


'''
6. Objeto datetime.strptime()
Converte a string para um objeto datetime.
Os atributos precisam estar no mesmo formato definido
'''
from datetime import datetime

datahora_string = '20/05/2025 19:01'
print(datahora_string, type(datahora_string))

datahora_convertida = datetime.strptime(datahora_string, '%d/%m/%Y %H:%M')
print(datahora_convertida, type(datahora_convertida))
print(7.2)

# Otimizando o código:

data_mascara_en = '%Y-%m-%d %H:%M'
data_mascara_ptbr = '%d/%m/%Y %H:%M'
datahora_local = datetime.now()
datahora_string = '2023-05-20 19:43'

print(datahora_local.strftime(data_mascara_ptbr))
print(datetime.strptime(datahora_string, data_mascara_en))
print()