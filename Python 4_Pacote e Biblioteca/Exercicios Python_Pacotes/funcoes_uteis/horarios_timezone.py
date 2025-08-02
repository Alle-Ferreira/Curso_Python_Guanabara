'''Funções Úteis - Dias e horários

1. Chamada de fuso horario com timezone'''

def fuso_brasilia():
    from datetime import datetime
    from zoneinfo import ZoneInfo  

    hora_bsb = datetime.now(ZoneInfo("America/Sao_Paulo"))    # list comprehension
    print(hora_bsb.strftime("%H:%M"))

    return hora_bsb

'''
# Main Program
horario_brasilia = fuso_brasilia()

# Outros fatiamentos com datetime:
print(horario_brasilia.year)
print(horario_brasilia.strftime("%d/%m"))'''

