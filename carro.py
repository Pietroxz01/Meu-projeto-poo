class Carro:
    def __init__(self, cor, marca, velocidade_atual, modelo):
        self.cor = cor
        self.marca = marca
        self.velocidade_atual = velocidade_atual
        self.modelo = modelo

    def acelerar(self, valor):
        self.velocidade_atual += valor
        print(f"Acelerando... Velocidade atual: {self.velocidade_atual} km/h")

    def frear(self, valor):
        if self.velocidade_atual - valor >= 0:
            self.velocidade_atual -= valor
        else:
            self.velocidade_atual = 0
        print(f"Freiando... Velocidade Atual: {self.velocidade_atual} km/h")

    def status(self):
        print("==== Status do Carro ====")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade Atual: {self.velocidade_atual}")
        print("======== ======== =======")

carro1 = Carro("preto", "ferrari", 50, "ferrari ")

carro1.status()

carro1.acelerar(50)

carro1.acelerar(200)