from datetime import datetime
from PackPOO1.extrato import Extrato    # "Extrato" é a classe e não o nome do arquivo


class Conta:
    def __init__(self, clientes, nr_conta, saldo):
        self.clientes = clientes
        self.nr_conta = nr_conta
        self.__saldo = saldo
        self.dt_abertura = datetime.today()
        self.extrato = Extrato()

    def depositar(self, vlr_deposito):      
        self.__saldo += vlr_deposito 
        self.extrato.transacoes.append(("Depósito", vlr_deposito, datetime.today()))               

    def sacar(self, vlr_saque):   
        if self.__saldo < vlr_saque:
            return False
        else:
            self.__saldo -= vlr_saque
            self.extrato.transacoes.append(("Saque", vlr_saque, datetime.today()))                 
            return True

    def transferir_vlr(self, conta_destino, vlr_transfer):
        if self.__saldo < vlr_transfer:
            return 'Saldo insuficiente para realizar a operação.'
        else:
            self.__saldo -= vlr_transfer
            conta_destino.depositar(vlr_transfer)
            self.extrato.transacoes.append(("Transferência", vlr_transfer, datetime.today()))         
            return 'Transferência realizada com sucesso.'

