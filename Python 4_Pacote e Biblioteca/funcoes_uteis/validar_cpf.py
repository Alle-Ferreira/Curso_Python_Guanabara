'''
Roteiro de prática Estacio - Modulo 2 / Atividade 2

1 - Regras de validação de um CPF. Confira!

a) Número de dígitos: Um CPF é composto por 11 dígitos numéricos.

b) Dígitos verificadores
Os dois últimos dígitos do CPF são chamados de dígitos verificadores, e são usados para garantir a integridade do número. 
Eles são calculados com base nos 9 primeiros dígitos do CPF.

c) Cálculo dos dígitos verificadores
Os dígitos verificadores são calculados usando o algoritmo de módulo 11. 
O primeiro dígito verificador é calculado a partir dos 9 primeiros dígitos do CPF. 
O segundo dígito verificador é calculado a partir dos 9 primeiros dígitos do CPF, incluindo o primeiro dígito verificador.

d) Validação dos dígitos verificadores
Após calcular os dígitos verificadores, eles são comparados com os dígitos originais do CPF. 
Se os dígitos verificadores calculados coincidirem com os dígitos verificadores originais, o CPF é considerado válido. 
Caso contrário, é considerado inválido.

d) Exceções
CPFs com todos os dígitos iguais (ex.: 111.111.111-11) ou CPFs com padrões específicos que foram anulados pela Receita Federal.

2 - Para realizar o exercício proposto, siga o passo a passo.

Crie um arquivo fonte chamado validacpf.
Crie uma função que:
- Remova os caracteres não numéricos.
- Valide a quantidade de dígitos do CPF.
- Valide se todos os dígitos não são iguais.
- Calcule o primeiro dígito verificador e o valide.
- Calcule o segundo dígito verificador e o valide.
- Teste a função passando um CPF como parâmetro.'''

def validar_cpf(cpf):

    cpf = ''.join(filter(str.isdigit, cpf))                 # Removendo caracteres não numéricos

    if len(cpf) != 11:                                      # Verificando se o CPF possui 11 dígitos
        return False

    if cpf == cpf[0] * 11:                                  # Verificando se todos os dígitos são iguais (caso raro, mas inválido)
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))    # Calculando o primeiro dígito verificador
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cpf[9]) != digito_verificador_1:                 # Verificando o primeiro dígito verificador
        return False

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))   # Calculando o segundo dígito verificador
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cpf[10]) != digito_verificador_2:                # Verificando o segundo dígito verificador
        return False

    return True                                             # CPF válido
 

cpf = "123.456.789-09"
if validar_cpf(cpf):
    print(f"O CPF {cpf} é válido.")
else:
    print(f"O CPF {cpf} é inválido.")
