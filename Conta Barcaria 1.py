class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito de R${valor} realizado! Novo Saldo: R${self.__saldo}")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado! Novo Saldo: R${self.__saldo}, Saldo atual da conto {self.__titular}: R${self.__saldo}")

    def get_saldo(self):
        print(f"Seu saldo é: R${self.__saldo}")

Nicole = ContaBancaria("Nicole", 1000)

Nicole.depositar(500)

Nicole.sacar(200)