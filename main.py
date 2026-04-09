from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/identificacao")
def ler_nome():
    return {
        "aluno": "Manuela Lobo",
        "rm": "24109798",  
        "projeto": "Desafio FastAPI - ADS"
    }