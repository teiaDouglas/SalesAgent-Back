from comparador import comparar_produtos
from busca_precos import buscar_precos

async def processar_consulta(descricao):
    produtos = await buscar_precos(descricao)
    comparativo = comparar_produtos(produtos)

    return {
        "descricao_original": descricao,
        "produtos_encontrados": produtos,
        "comparativo": comparativo,
        "sugestoes": gerar_sugestoes(descricao)
    }

def gerar_sugestoes(descricao):
    if "polegadas" in descricao:
        base = int(descricao.split()[1])
        return [f"TV {base - 5} polegadas", f"TV {base + 5} polegadas"]
    return []
