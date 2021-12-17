class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"{self.nome} - {self.salario} reais"

    def aumentar_salario(self, porcentagem):
        self.salario += self.salario * (porcentagem/100)


funcionario = Funcionario("João", 3000)
print(funcionario)
funcionario.aumentar_salario(10)
print(funcionario)
