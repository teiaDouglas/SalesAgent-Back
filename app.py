from fastapi import FastAPI
from pydantic import BaseModel
from agente_openai import consulta_openai
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique ['http://localhost:5173'] se quiser mais segurança
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Consulta(BaseModel):
    descricao: str

@app.post("/consulta")
async def consultar_produto(consulta: Consulta):
    resposta = await consulta_openai(consulta.descricao)
    return {"resposta": resposta}
