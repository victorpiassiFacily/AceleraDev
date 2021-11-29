class Pessoa:
    def __init__(self, nome, documento):
        self.nome = nome
        self.documento = documento


class Conta:
    def __init__(self, numero, agencia, titular):
        self.numero = numero
        self.agencia = agencia
        self._saldo = 0
        self.titular = titular

    def sacar(self, valor):
        self._saldo -= valor

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def exibir_saldo(self):
        print(f'A conta do {self.titular.nome} é de: R$ {self.saldo}')


class ContaCorrente(Conta):
    def __init__(self, numero, agencia, titular):
        self.__saques = 0
        super().__init__(numero, agencia, titular)

    def sacar(self, valor):
        self.__saques += 1
        if self.__saques > 3:
            self._saldo -= self._saldo * 0.001
        self._saldo -= valor


class ContaPoupanca(Conta):
    pass


ana = Pessoa('Ana', '0000012')
joao = Pessoa('João', '0000123')

conta_corrente = ContaCorrente('123', '01', ana)
conta_corrente.depositar(100)
conta_corrente.sacar(10)
conta_corrente.sacar(10)
conta_corrente.sacar(10)
conta_corrente.sacar(10)
print(conta_corrente.exibir_saldo())

conta_poupanca = ContaPoupanca('456', '01', joao)
conta_poupanca.depositar(100)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)
conta_poupanca.sacar(10)

print(conta_poupanca.exibir_saldo())
