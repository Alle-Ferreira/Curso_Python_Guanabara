#Operadores Logicos
#São operadores usados junto com operadores de comparação, para montar uma expressao logica

#Exemplos
saldo=1000
saque=200
limite=100

print(saldo >= saque)
print(saque <= limite)
#Dá apenas uma resposta binária (True/False), apos avaliar as afirmativas acima.
print()

#Operador "And": todas as condições precisam ser verdadeiras
print('Operador AND:')
print('true and true = true')
print('true and false = false')
print('false and false = false')
print(saldo >= saque and saque <= limite)
print()

#Operador "Or": apenas uma condição precisa ser verdadeira
print('Operador OR')
print('true or true = true')
print('true or false = true')
print('false or false = false')
print(saldo >= saque or saque <= limite)
print()

#Operador "Not"
print('Operador NOT')

print(not 1000 > 1500)
# 1000 é < 1500 (false), mas com a negativa do NOT, vira TRUE

contatos_emergencia = []
print(not contatos_emergencia)
#lista [] vazia em Python tem valor booleano FALSE. Com a negativa, vira TRUE

print(not "saque 1500;")
#string com conteúdo é TRUE, mas com a negativa vira FALSE

print(not "")
#string vazia é FALSE, mas com a negativa vira TRUE
print()

#Parenteses: melhores praticas
print('Parênteses: melhores praticas')
saldo=1000
saque=250
limite=200
conta_especial=True

exp1 = saldo>=saque and saque<=limite or conta_especial and saldo >= saque
exp2 = (saldo>=saque and (saque<=limite or conta_especial) and saldo >= saque)
exp3 = (saldo>=saque and saque<=limite) or (conta_especial and saldo >= saque)

print(exp1)
print(exp2)
print(exp3)
print()

#Exercicio Pratico
print("Exercicio Pratico")
#Expressoes curtas: melhores praticas
print('Expressoes curtas: melhores praticas')
print()

#Exemplo 1
#Resultado será FALSE pq o saque é maior que o limite diário
saldo=1000
saque=300
limite_saque_dia=200
limite_especial=500
conta_regular = (saldo>=saque and saque<=limite_saque_dia)
conta_especial = (limite_especial>=saque and saque<=limite_saque_dia) or conta_regular
saque_liberado = conta_regular or conta_especial
print(saque_liberado)
print()

#Exemplo 2
#Resultado será TRUE pois todas as condições serão válidas

saldo=1000
saque=250
limite_saque_dia=300
limite_especial=500

conta_regular = (saldo>=saque and saque<=limite_saque_dia)
conta_especial = (limite_especial>=saque and saque<=limite_saque_dia) or conta_regular
saque_liberado = conta_regular or conta_especial

print(saque_liberado)
#Resultado será FALSE pq o saque é maior que o limite diário
print()
