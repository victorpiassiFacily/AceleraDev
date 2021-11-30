from typing import List, Optional
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


def categoria():
    class BaseCategoriaModel(BaseModel):
        nome: str
        produtos: List[int]

    class IndexCategoriaModel(BaseCategoriaModel):
        cod_categoria: int

    class AlterarCategoriaModel(BaseCategoriaModel):
        pass

    categorias: IndexCategoriaModel = []

    @app.post('/categoria', status_code=status.HTTP_201_CREATED)
    def adicionar_categoria(categoria: BaseCategoriaModel):

        index_categoria = IndexCategoriaModel(
            nome=categoria.nome,
            produtos=categoria.produtos,
            cod_categoria=len(categorias) + 1
        )

        categorias.append(index_categoria)

        return index_categoria

    @app.get('/categoria')
    def lista_categorias():
        return categorias

    @app.get('/categoria/{cod_categoria}')
    def mostrar_categoria(cod_categoria: int):

        categoria = list(
            filter(lambda a: a.cod_categoria == cod_categoria, categorias)
        )

        return categoria

    @app.delete('/categoria/{cod_categoria}', status_code=status.HTTP_204_NO_CONTENT)
    def remover_categoria(cod_categoria: int):

        resultado = list(filter(
            lambda a: a[1].cod_categoria == cod_categoria, enumerate(
                categorias)
        ))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de categoria {cod_categoria} não encontrado!'
            )

        i, _ = resultado[0]
        del categorias[i]

    @app.put('/categoria/{cod_categoria}')
    def alterar_categoria(cod_categoria: int, categoria: AlterarCategoriaModel):

        resultado = list(
            filter(lambda a: a.cod_categoria == int(cod_categoria), categorias)
        )

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de categoria {cod_categoria} não encontrado!'
            )

        categoria_encontrado = resultado[0]
        categoria_encontrado.nome = categoria.nome
        categoria_encontrado.produtos = categoria.produtos

        return categoria_encontrado

    @app.patch('/categoria/cod-categoria/{cod_categoria}')
    def alterar_cod_categoria_categoria(cod_categoria: int, cod_categoria_novo: int = Body(..., embed=True)):

        resultado = list(
            filter(lambda a: a.cod_categoria == cod_categoria, categorias))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de categoria {cod_categoria} não encontrado!'
            )

        categoria_encontrado = resultado[0]
        categoria_encontrado.cod_categoria = cod_categoria_novo

        return categoria_encontrado
