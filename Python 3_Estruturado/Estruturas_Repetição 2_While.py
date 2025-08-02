''' Estruturas de Repetição: WHILE

Permite executar repetidamente um bloco de código enquanto uma condição for verdadeira. 
    
1. WHILE com condição de parada
A sintaxe do while é a apresentada a seguir:

while condição:
    bloco_de_codigo
    
'''

palavra = input('Entre com uma palavra: \n')
while palavra != 'sair':
    palavra = input('Digite "sair" para encerrar o laço: \n')
print('Você digitou "sair" e agora está fora do laço')


opcao = -1
while opcao != 0:
    opcao = int (input("[1] Sacar \n[2] Extrato \n[0] Sair \n: ")) 
    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo o extrato...')
else:
    print('Obrigada por usar nosso sistema bancário, até logo!')


'''
2. WHILE em laço infinito - True
Laços infinitos são úteis quando queremos executar um bloco de instruções indefinidamente.
Portanto, necessário cuidado, para evitar problemas de consumo excessivo de memória. 

Sintaxes laço while infinito:

while True:
    bloco_de_codigo
'''
    
# while True:
#     temperatura = ler_sensor_temperatura()      # Supomos que esta função leia a temperatura do sensor
#     registrar_temperatura(temperatura)          # Supomos que esta função registre a temperatura lida
#     time.sleep(60)                              # "Segura" a aplicação por 1min, até a proxima leitura.

