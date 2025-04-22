import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def formatar_nome_para_url(nome):
    return nome.replace(" ", "-").lower()

async def buscar_precos(descricao):
    resultados_zoom = buscar_zoom(descricao)
    resultados_ml = buscar_mercado_livre(descricao)
    return resultados_zoom + resultados_ml

def buscar_zoom(descricao):
    try:
        termo = formatar_nome_para_url(descricao)
        url = f"https://www.zoom.com.br/search?q={termo}"

        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        produtos = []

        for item in soup.select(".ProductCard_ProductCard__content__info__name__2L8Oa"):
            nome = item.text.strip()
            link_tag = item.find_parent("a")
            if not link_tag:
                continue

            link = "https://www.zoom.com.br" + link_tag["href"]
            preco_tag = item.find_parent("div").find_next("p")
            preco = preco_tag.text.strip() if preco_tag else "Preço não encontrado"

            produtos.append({
                "site": "Zoom",
                "nome": nome,
                "preco": preco,
                "url": link
            })

        return produtos
    except Exception as e:
        print(f"[ERRO ZOOM] {e}")
        return []


def buscar_mercado_livre(descricao):
    try:
        termo = descricao.replace(" ", "-")
        url = f"https://lista.mercadolivre.com.br/{termo}"
        print(f"{url}")  # type: ignore # DEBUG
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        produtos = []

        for item in soup.select(".ui-search-result__wrapper"):
            titulo_tag = item.select_one(".ui-search-item__title")
            preco_tag = item.select_one(".ui-search-price__part")
            link_tag = item.find("a", href=True)

            if titulo_tag and preco_tag and link_tag:
                produtos.append({
                    "site": "Mercado Livre",
                    "nome": titulo_tag.text.strip(),
                    "preco": preco_tag.text.strip(),
                    "url": link_tag["href"]
                })

        return produtos
    except Exception as e:
        print(f"[ERRO MERCADO LIVRE] {e}")
        return []
