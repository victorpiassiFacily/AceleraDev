class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, qtdCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdCombustivel = qtdCombustivel

    def __str__(self):
        return f"{self.tipoCombustivel} ({self.qtdCombustivel} litros) - {self.valorLitro} R$"

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        self.qtdCombustivel -= litros
        return litros

    def abastecerPorLitro(self, litros):
        self.qtdCombustivel -= litros
        return litros * self.valorLitro

    def alterarValor(self, valor):
        self.valorLitro = valor

    def alterarCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterarQtdCombustivel(self, qtdCombustivel):
        self.qtdCombustivel = qtdCombustivel


bombaCombustivel = BombaCombustivel("alcool", 7, 500)
print(bombaCombustivel)
print(f"{bombaCombustivel.abastecerPorValor(150)} litros")
print(f"{bombaCombustivel.abastecerPorLitro(20)} reais")

bombaCombustivel.alterarCombustivel("gasolina")
bombaCombustivel.alterarValor(9)
bombaCombustivel.alterarQtdCombustivel(700)
print(bombaCombustivel)
