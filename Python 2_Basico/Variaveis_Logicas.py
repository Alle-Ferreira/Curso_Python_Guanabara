# Variaveis Logicas

# Exemplo 1
nome='Alle'
salario=1500
aumento=0.05
novo_salario=(salario+(salario*aumento))
print('Olá,',nome,'!')
print('O aumento de salário foi de',(aumento*100),'%.')
print(nome,'seu novo salário é de',novo_salario,'reais.')
print()

# Exemplo 2
aumento2=0.15
frase_input = 'Você não é '+nome+'. Quem é você? '
nome2=input(frase_input)
salario2=int (input('Qual é o seu salário? '))
novo_salario2=(salario2+(salario2*aumento2))
print()

print(nome2,'seu salario anterior era de ',salario2,'reais.')
print('E você recebeu um aumento de ',(aumento2*100),'%.')
print(nome2,'seu novo salário é de',novo_salario2)
print()