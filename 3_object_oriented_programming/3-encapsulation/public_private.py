class Conta:
    def __init__(self, saldo):
        self._saldo = saldo # Python convention: anything with an _ indicates private privacy.
    
    def deposito (self, valor):
        self._saldo += valor
    
    def sacar (self, valor):
        self._saldo -= valor

vinicius_conta = Conta(1000)
vinicius_conta.deposito(10)
vinicius_conta.sacar(100)

print(vinicius_conta._saldo)

