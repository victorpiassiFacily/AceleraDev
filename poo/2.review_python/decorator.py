def printer(func):
    print(f'chamando a funcao {func.__name__}')
    return func


@printer
def soma(a, b):
    return a + b


@printer
def hello(name):
    print(f'Hello {name}')


print(soma(2, 2))
hello('matheus')
