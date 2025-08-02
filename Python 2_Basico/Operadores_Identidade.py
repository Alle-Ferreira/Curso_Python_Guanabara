#Operadores de Identidade

curso = "Curso de Pyhton"
nome_curso = curso
saldo, limite = 200, 200

print (curso is nome_curso)
#True
print (curso is not nome_curso)
#False
print (saldo is limite)
#True
print()

#Exercicio Pratico
print("Exercicio Pratico")

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
print()

#Exercicio Free Style
print('Exercicio Free Style')
curso = "Curso de Python"
nr_hs_curso = 60
print()

#Aluno1
print('Aluno 1')
nome_curso_aluno = "Curso de Python"
nr_hs_aluno = 60

curso_liberado = (curso is nome_curso_aluno) and (nr_hs_curso<=nr_hs_aluno)
print(curso_liberado)
print()

#Aluno2
print('Aluno 2')
nome_curso_aluno = "Curso de Python"
nr_hs_aluno = 40

curso_liberado = (curso is nome_curso_aluno) and (nr_hs_curso<=nr_hs_aluno)
print(curso_liberado)
print()