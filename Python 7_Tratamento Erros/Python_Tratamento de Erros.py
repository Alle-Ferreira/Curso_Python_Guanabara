'''
1. Erros em um programa Python

Tipos de erros: erros de sintaxe, exceções e falhas de lógica.

a) Os erros de sintaxe são aqueles que ocorrem devido ao formato incorreto de uma instrução. Esses erros são descobertos pelo componente do interpretador Python, que é chamado analisador ou parser.

b) Os erros que ocorrem em tempo de execução do programa, que se devem nao a uma instrução escrita errada, e sim ao fato de que o programa entrou em um estado indevido. Neste caso é dito que o interpretador Python levanta uma exceção: 

- A divisão por 0.
- A tentativa de acessar um índice indevido em uma lista.
- Um nome de variável não atribuído.
- Um erro causado por tipos incorretos de operando.


Exceção	            Explicação

KeyboardInterrupt	Levantado quando o usuário pressiona CTRL+C, a combinação de interrupção.
OverflowError	    Levantado quando uma expressão de ponto flutuante é avaliada como um valor muito grande.
ZeroDivisionError	Levantado quando se tenta dividir por 0.
IOError	            Levantado quando uma operação de entrada/saída falha por um motivo relacionado a isso.
IndexError	        Levantado quando um índice sequencial está fora do intervalo de índices válidos.
NameError	        Levantado quando se tenta avaliar um identificador (nome) não atribuído.
TypeError	        Levantado quando uma operação da função é aplicada a um objeto do tipo errado.
ValueError	        Levantado quando a operação ou função tem um argumento com o tipo correto, mas valor incorreto.


Em Python, as exceções são objetos. A classe Exception é derivada de BaseException, classe base de todas as classes de exceção. 
BaseException fornece alguns serviços úteis para todas as classes de exceção, mas normalmente não se torna uma subclasse diretamente.


2. Exceçoes

O formato padrão de uso do par try/except é:

O bloco 1 representa o fluxo normal do programa. 
Caso uma exceção seja levantada, o bloco 2 será executado, permitindo o tratamento adequado dela. Esse bloco 2 é chamado de manipulador de exceção.

try:
   Bloco 1
except:
   Bloco 2
Instrução fora do try/except
'''

# Exemplo 1:

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except NameError:
    print("Entre com o valor numérico e não letras")


# Exemplo 2:

try:                                               # tentativa de execução
   numerador = int(input('Numerador: '))
   denominador = int(input('Denominador: '))
   resultado = numerador/denominador
except:                                            # ação qdo execução a tentativa falha
   print('Ocorreu um erro. Programa encerrado.')
else:                                              # ação qdo exceção não ocorre
   print(f'Resultado: {resultado:.2f}')
finally:                                           # sempre executado
   print('Obrigada!')


# Exemplo 3:

try:                                               # tentativa de execução
   numerador = int(input('Numerador: '))
   denominador = int(input('Denominador: '))
   resultado = numerador/denominador
except (ValueError, TypeError):                    # especifica o tipo de exceção
   print('Entrada inválida.')
except ZeroDivisionError:                          # especifica o tipo de exceção
   print('Não é possível dividir por zero.')
except KeyboardInterrupt:                          # especifica o tipo de exceção
   print('Programa foi interrompido via teclado.')
else:                                              # ação qdo exceção não ocorre
   print(f'Resultado: {resultado:.2f}')
finally:                                           # sempre executado
   print('Obrigada!')