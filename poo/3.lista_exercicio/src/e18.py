class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def __str__(self):
        return f"{self.combustivel} ({self.consumo} km/l)"

    def andar(self, quilometros):
        combustivel_consumido = quilometros / self.consumo
        print(combustivel_consumido)
        self.combustivel -= combustivel_consumido

    def obterGasolina(self):
        return f"{self.combustivel} litros"

    def adicionarGasolina(self, combustivel):
        self.combustivel += combustivel


carro = Carro(6)
carro.adicionarGasolina(50)
print(carro)
carro.andar(60)
print(carro)
