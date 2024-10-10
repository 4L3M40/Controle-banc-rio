class Conta:
    def __init__(self, titular, numero, saldo=0):
        self._saldo = saldo
        self.numero = numero
        self.titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("O Saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"Cliente: {self.titular}, Saldo Atual: {self.saldo}")
