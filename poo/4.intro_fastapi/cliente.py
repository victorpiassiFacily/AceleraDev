from typing import List, Optional
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


def cliente():
    class Cartao():
        conta: str
        agencia: str
        digito: int
        cod_seguranca: int
        validade: str

    class BaseClienteModel(BaseModel):
        nome: str
        endereco: str
        cep: str
        cartao: Cartao

    class AdicionarClienteModel(BaseClienteModel):
        cpf: int

    class AlterarClienteModel(BaseClienteModel):
        pass

    clientes: AdicionarClienteModel = []

    @app.post('/cliente', status_code=status.HTTP_201_CREATED)
    def adicionar_cliente(cliente: AdicionarClienteModel):
        clientes.append(cliente)

    @app.get('/cliente')
    def lista_clientes():
        return clientes

    @app.get('/cliente/{cpf}')
    def mostrar_cliente(cpf: int):

        cliente = list(
            filter(lambda a: a.cpf == cpf, clientes)
        )

        return cliente

    @app.delete('/cliente/{cpf}', status_code=status.HTTP_204_NO_CONTENT)
    def remover_cliente(cpf: int):

        resultado = list(filter(
            lambda a: a[1].cpf == cpf, enumerate(clientes)
        ))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de cliente {cpf} não encontrado!'
            )

        i, _ = resultado[0]
        del clientes[i]

    @app.put('/cliente/{cpf}')
    def alterar_cliente(cpf: int, cliente: AlterarClienteModel):

        resultado = list(filter(
            lambda a: a.cpf == cpf, clientes)
        )

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de cliente {cpf} não encontrado!'
            )

        cliente_encontrado = resultado[0]
        cliente_encontrado.nome = cliente.nome
        cliente_encontrado.endereco = cliente.endereco
        cliente_encontrado.cep = cliente.cep
        cliente_encontrado.cartao = cliente.cartao

        return cliente_encontrado

    @app.patch('/cliente/cpf/{cpf}')
    def alterar_cpf_cliente(cpf: int, cpf_novo: int = Body(..., embed=True)):

        resultado = list(
            filter(lambda a: a.cpf == cpf, clientes))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de cliente {cpf} não encontrado!'
            )

        cliente_encontrado = resultado[0]
        cliente_encontrado.cpf = cpf_novo

        return cliente_encontrado
