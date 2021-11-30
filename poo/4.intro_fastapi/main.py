from typing import List, Optional
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Path
from fastapi.params import Body
from pydantic import BaseModel

from produto import produto
from categoria import categoria

app = FastAPI()


############################
############################
######### PRODUTO ##########
############################
############################


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


############################
############################
######## CATEGORIA #########
############################
############################


class BaseCategoriaModel(BaseModel):
    nome: str
    produtos: List


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


class Cartao(BaseModel):
    conta: str
    agencia: str
    digito: int
    cod_seguranca: int
    validade: str


class BaseClienteModel(BaseModel):
    nome: str
    endereco: str
    cep: str
    # cartao: Cartao


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
    # cliente_encontrado.cartao = cliente.cartao

    return cliente_encontrado


@app.patch('/cliente/cpf/{cpf}')
def alterar_cpf_cliente(cpf: int, cpf_novo: int = Body(..., embed=True)):

    resultado = list(
        filter(lambda a: a.cpf == int(cpf), clientes))

    if not resultado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Código de cliente {cpf} não encontrado!'
        )

    cliente_encontrado = resultado[0]
    cliente_encontrado.cpf = cpf_novo

    return cliente_encontrado
