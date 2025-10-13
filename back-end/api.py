from fastapi import FastAPI
import funcao 

#Rodar o fastapi
#python -m uvicorn api:app --reload

#Testa api Fastapi
# /docs > Documnetação Swagger
# /redoc > Documentação redoc

#Iniciar o fastapi 
app = FastAPI(title="Gerenciador de filmes")

#GET = Pegar / listar
#POST = criar / enviar
#PUT =Atualizar
#DELETE = deletar

@app.get("/")
def home():
    return {"mensagem": "Quero café prof"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filmes(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}