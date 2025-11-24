class Conta:
    def __init__(self, saldo=None):
        self._saldo = saldo
    
    @property
    def saldo(self):
        return self._saldo or 0

    @saldo.setter
    def saldo(self, valor):
        self._saldo += valor

    # @saldo.setter
    # def saldo(self, valor):
    #     self._saldo -= valor

    @saldo.deleter
    def saldo(self):
        self._saldo = -1


conta = Conta(10)
print(conta.saldo)
conta.saldo = 10
print(conta.saldo)
del conta.saldo
print(conta.saldo)