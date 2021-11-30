from typing import List, Optional
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


def fornecedor():
    class BaseFornecedorModel(BaseModel):
        nome: str
        endereco: str
        cep: str

    class AdicionarFornecedorModel(BaseFornecedorModel):
        cnpj: int

    class AlterarFornecedorModel(BaseFornecedorModel):
        pass

    fornecedores: AdicionarFornecedorModel = []

    @app.post('/fornecedor', status_code=status.HTTP_201_CREATED)
    def adicionar_fornecedor(fornecedor: AdicionarFornecedorModel):
        fornecedores.append(fornecedor)

    @app.get('/fornecedor')
    def lista_fornecedores():
        return fornecedores

    @app.get('/fornecedor/{cnpj}')
    def mostrar_fornecedor(cnpj: int):

        fornecedor = list(
            filter(lambda a: a.cnpj == cnpj, fornecedores)
        )

        return fornecedor

    @app.delete('/fornecedor/{cnpj}', status_code=status.HTTP_204_NO_CONTENT)
    def remover_fornecedor(cnpj: int):

        resultado = list(filter(
            lambda a: a[1].cnpj == cnpj, enumerate(fornecedores)
        ))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de fornecedor {cnpj} não encontrado!'
            )

        i, _ = resultado[0]
        del fornecedores[i]

    @app.put('/fornecedor/{cnpj}')
    def alterar_fornecedor(cnpj: int, fornecedor: AlterarFornecedorModel):

        resultado = list(filter(
            lambda a: a.cnpj == int(cnpj), fornecedores)
        )

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de fornecedor {cnpj} não encontrado!'
            )

        fornecedor_encontrado = resultado[0]
        fornecedor_encontrado.nome = fornecedor.nome
        fornecedor_encontrado.endereco = fornecedor.endereco
        fornecedor_encontrado.cep = fornecedor.cep

        return fornecedor_encontrado

    @app.patch('/fornecedor/cnpj/{cnpj}')
    def alterar_cnpj_fornecedor(cnpj: int, cnpj_novo: int = Body(..., embed=True)):

        resultado = list(
            filter(lambda a: a.cnpj == cnpj, fornecedores))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de fornecedor {cnpj} não encontrado!'
            )

        fornecedor_encontrado = resultado[0]
        fornecedor_encontrado.cnpj = cnpj_novo

        return fornecedor_encontrado
