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
    return {"mensagem": "Bem-Vindo ao Gerenciador de Filmes"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.inserir_filmes(titulo, genero, ano, avaliacao)
    return { "mensagem": "Filme adicionado com sucesso!"}

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filmes()
    lista = []
    for linha in filmes:
        lista.append({ 
            "id": linha[0],
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avalicao": linha[4] 
            })
    return {"filmes": lista}

@app.put("/filmes/{id_filme}")
def atualizar_filme(id_filme: int, nova_avaliacao: float):
    filme = funcao.buscar_filme(id_filme)
    if filme:
        funcao.atualizar_filme(id_filme, nova_avaliacao)
        return {"mensagem": "Filme atualizado com sucesso!"}
    else:
        return { "erro": "Filme não encontrado"}