from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"msg": "hello"}

@app.get("/soma")
def soma(a: int, b: int):
    return a + b