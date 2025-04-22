def comparar_produtos(produtos):
    comparativo = []
    for produto in produtos:
        comparativo.append({
            "modelo": produto["modelo"],
            "marca": produto["marca"],
            "preco": produto["preco"],
            "vantagens": gerar_vantagens(produto),
        })
    return comparativo

def gerar_vantagens(produto):
    if "UHD" in produto["modelo"]:
        return ["Alta resolução", "Bom para filmes"]
    elif "NanoCell" in produto["modelo"]:
        return ["Boa qualidade de imagem", "Cores vivas"]
    return ["Básico"]
