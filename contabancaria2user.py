class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f"Depósito de R${valor} realizado! Saldo atual: R${self.__saldo}")
            print(f"Depósito de R${valor} realizado! Novo Saldo: R${self.__saldo}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return
        if valor > self.__saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        self.__saldo -= valor
        self.__historico.append(f"Saque de R${valor} realizado! Saldo atual: R${self.__saldo}")
        print(f"Saque de R${valor} realizado! Novo Saldo: R${self.__saldo}")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("O valor da transferência deve ser maior que zero.")
            return
        if valor > self.__saldo:
            print("Saldo insuficiente para realizar a transferência.")
            return
        if not isinstance(conta_destino, ContaBancaria):
            print("Conta de destino inválida.")
            return
        
        self.__saldo -= valor
        conta_destino.depositar(valor)
        self.__historico.append(f"Transferência de R${valor} para {conta_destino.titular} realizada! Saldo atual: R${self.__saldo}")
        conta_destino.__historico.append(f"Recebido R${valor} de {self.__titular}. Saldo atual: R${conta_destino.saldo}")

    def ver_historico(self):
        print(f"Histórico de transações para {self.__titular}:")
        for transacao in self.__historico:
            print(transacao)

# Testando a classe
Nicole = ContaBancaria("Nicole", 1000)
Nicole.depositar(500)
Nicole.sacar(200)

# Criando outra conta para transferências
Lucas = ContaBancaria("Lucas", 300)
Nicole.transferir(300, Lucas)

# Verificando o histórico de transações
Nicole.ver_historico()
Lucas.ver_historico()