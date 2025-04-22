import openai
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()

# Usa a chave da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")
async def consulta_openai(descricao):
    prompt = f"""
Você é um assistente especialista em produtos eletroeletrônicos. Um vendedor te pergunta sobre o seguinte produto: "{descricao}".

1. Liste pelo menos 3 modelos reais que se encaixem nessa descrição.
2. Mostre suas características técnicas.
3. Compare marcas diferentes (como Samsung vs LG, etc).
4. Dê uma estimativa de preço por modelo.
5. Sugira tamanhos alternativos se aplicável.
6. Use linguagem clara e objetiva, voltada para ajudar o vendedor a explicar ao cliente.
7. Responda em formato de json estruturado.
8. O Modelo do Json a ser utilizado é igual abaixo. As especificações devem variar de acordo com o produto:



{{
  "produto": {{
    "nome": "iPhone 11",
    "descricao": "Descrição breve do produto",
    "modelos": [
      {{
        "modelo": "iPhone 11",
        "preco": "A partir de $699",
        "especificacoes": {{
          "tela": "6.1 polegadas Liquid Retina HD",
          "processador": "A13 Bionic",
          "camera_traseira": "Dupla de 12 MP com ultra wide e zoom óptico de 2x",
          "camera_frontal": "12 MP TrueDepth",
          "armazenamento": "64GB, 128GB, 256GB",
          "bateria": "Até 17 horas de reprodução de vídeo",
          "resistencia_agua": "Até 2 metros por até 30 minutos"
        }}
      }},
      {{
        "modelo": "iPhone 11 Pro",
        "preco": "A partir de $999",
        "especificacoes": {{
          "tela": "5.8 polegadas Super Retina XDR",
          "processador": "A13 Bionic",
          "camera_traseira": "Tripla de 12 MP com ultra wide, wide e teleobjetiva",
          "camera_frontal": "12 MP TrueDepth",
          "armazenamento": "64GB, 256GB, 512GB",
          "bateria": "Até 18 horas de reprodução de vídeo",
          "resistencia_agua": "Até 4 metros por até 30 minutos"
        }}
      }},
      {{
        "modelo": "iPhone 11 Pro Max",
        "preco": "A partir de $1099",
        "especificacoes": {{
          "tela": "6.5 polegadas Super Retina XDR",
          "processador": "A13 Bionic",
          "camera_traseira": "Tripla de 12 MP com ultra wide, wide e teleobjetiva",
          "camera_frontal": "12 MP TrueDepth",
          "armazenamento": "64GB, 256GB, 512GB",
          "bateria": "Até 20 horas de reprodução de vídeo",
          "resistencia_agua": "Até 4 metros por até 30 minutos"
        }}
      }}
    ]
  }}
}}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",  # ou "gpt-3.5-turbo" se quiser mais rápido/barato
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message["content"]
