from typing import List, Optional
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


def produto():
    class BaseProdutoModel(BaseModel):
        nome: str
        descricao: Optional[str] = None
        categoria: int
        preco: int
        quantidade: int
        promocao: Optional[int] = None

    class IndexProdutoModel(BaseProdutoModel):
        cod_produto: int

    class AlterarProdutoModel(BaseProdutoModel):
        pass

    produtos: IndexProdutoModel = []

    @app.post('/produto', status_code=status.HTTP_201_CREATED)
    def adicionar_produto(produto: BaseProdutoModel):

        index_produto = IndexProdutoModel(
            nome=produto.nome,
            descricao=produto.descricao,
            categoria=produto.categoria,
            preco=produto.preco,
            quantidade=produto.quantidade,
            promocao=produto.promocao,
            cod_produto=len(produtos) + 1
        )

        produtos.append(index_produto)

        return index_produto

    @app.get('/produto')
    def lista_produtos():
        return produtos

    @app.get('/produto/{cod_produto}')
    def mostrar_produto(cod_produto: int):
        produto = list(
            filter(lambda a: a.cod_produto == cod_produto, produtos))
        return produto

    @app.delete('/produto/{cod_produto}', status_code=status.HTTP_204_NO_CONTENT)
    def remover_produto(cod_produto: int):

        resultado = list(filter(
            lambda a: a[1].cod_produto == cod_produto, enumerate(produtos)
        ))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de produto {cod_produto} não encontrado!'
            )

        i, _ = resultado[0]
        del produtos[i]

    @app.put('/produto/{cod_produto}')
    def alterar_produto(cod_produto: int, produto: AlterarProdutoModel):

        resultado = list(
            filter(lambda a: a.cod_produto == int(cod_produto), produtos)
        )

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de produto {cod_produto} não encontrado!'
            )

        produto_encontrado = resultado[0]
        produto_encontrado.nome = produto.nome
        produto_encontrado.descricao = produto.descricao
        produto_encontrado.categoria = produto.categoria
        produto_encontrado.preco = produto.preco
        produto_encontrado.quantidade = produto.quantidade
        produto_encontrado.promocao = produto.promocao

        return produto_encontrado

    @app.patch('/produto/cod-produto/{cod_produto}')
    def alterar_cod_produto_produto(cod_produto: int, cod_produto_novo: int = Body(..., embed=True)):

        resultado = list(
            filter(lambda a: a.cod_produto == cod_produto, produtos))

        if not resultado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Código de produto {cod_produto} não encontrado!'
            )

        produto_encontrado = resultado[0]
        produto_encontrado.cod_produto = cod_produto_novo

        return produto_encontrado
