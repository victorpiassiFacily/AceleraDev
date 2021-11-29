from typing import List


class Cliente:
    def __init__(self, nome, identidade):
        self.nome = nome
        self.identidade = identidade

    def __str__(self):
        return f'Nome: {self.nome} [{self.identidade}]'


class Produto:
    def __init__(self, codigo: str, descricao: str, valor_unitario: float, quantidade: float, desconto: float):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.quantidade = quantidade
        self.desconto = desconto

    def valor_final(self):
        return self.valor_unitario * self.quantidade

    def valor_com_desconto(self):
        valor_final = self.valor_unitario * self.quantidade
        return valor_final - (valor_final * (self.desconto/100))

    def __str__(self):
        return f'{self.codigo}: {self.descricao}, R$ {self.valor_unitario} ({self.quantidade})'


class Carrinho:
    def __init__(self):
        self._cliente = None
        self._itens: List[Produto] = []

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    def add_item(self, produto):
        self._itens.append(produto)

    def remover_item(self, codigo):
        resultado = list(
            filter(lambda i: i[1].codigo == codigo, enumerate(self._itens)))
        if resultado:
            indice, _ = resultado[0]
            del self._itens[indice]

    def incrementar_item(self, codigo, quantidade=1):
        resultado = list(
            filter(lambda i: i.codigo == codigo, self._itens))

        if resultado:
            produto = resultado[0]
            if produto.quantidade <= 3:
                produto.quantidade += quantidade

    def decrementar_item(self, codigo, quantidade=1):
        resultado = list(
            filter(lambda i: i.codigo == codigo, self._itens))

        if resultado:
            produto = resultado[0]
            if produto.quantidade == 1 or quantidade > produto.quantidade:
                self.remover_item(codigo)
            else:
                produto.quantidade -= quantidade

    def total_carrinho(self):
        valores = [p.valor_final() for p in self._itens]
        return sum(valores)

    def exibir_itens(self):
        print('Itens no carrinho:')
        for item in self._itens:
            print(item)

    def total_com_desconto(self):
        valores = [p.valor_com_desconto() for p in self._itens]
        return sum(valores)

    def exibir_resumo(self):
        print('Resumo:')
        print(f'Cliente: {self.cliente}')
        print(f'Itens: ({len(self._itens)})')
        for item in self._itens:
            print(item)
        print('-----------')
        print(f'Valor total: {self.total_carrinho()}')
        print(f'Total com desconto {self.total_com_desconto()}')
