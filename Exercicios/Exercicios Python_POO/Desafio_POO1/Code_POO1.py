'''Desafio de Codigo - Parte 1: com AGREGAÇÃO / ASSOCIAÇÃO

Desafio de Codigo - Parte 2: COMPOSIÇÃO

A existencia de um, depende da pre-existencia de outro. Exemplo:
- Para ter Extrato precisa ter uma Conta
'''

from PackPOO1.cliente import Cliente    # "Cliente" é a classe e não o nome do arquivo
from PackPOO1.conta import Conta        # "Conta" é a classe e não o nome do arquivo


cliente1 = Cliente('123456789-01', 'Camila Algarves', 'Rua das Araucarias, 102')
cliente2 = Cliente('234567890-12', 'Mariana Nogueira', 'Avenida Paulista, 1.209')
cliente3 = Cliente('345678901-23', 'Carlos Alberto', 'Qd 03, Rua 18')

conta1 = Conta([cliente1, cliente2], '100-1', 1200.35 )         # cria uma [lista] para a conta conjunta.
conta2 = Conta(cliente3, '100-2', 1000.35 )                     

conta1.depositar(1000)
conta1.sacar(500)

conta2.depositar(1100)
conta2.sacar(300)
conta2.transferir_vlr(conta1, 150)

conta1.extrato.exibir_extrato(conta1.nr_conta)   
conta2.extrato.exibir_extrato(conta2.nr_conta)   
# "extrato" aqui é um atributo da classe Conta.
# "conta1" define de qual conta será o extrato.
# "conta1.nr_conta" passa o numero da conta, a ser usado na string de exibição.