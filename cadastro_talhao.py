# Modulo: cadastro de talhoes - App AgroGestao
# Artefato criado para atender solicitacao do time de operacoes

def cadastrar_talhao(nome, area_ha, cultura):
    """Cadastra um talhao da fazenda com area (hectares) e cultura."""
    if area_ha <= 0:
        raise ValueError("A area do talhao deve ser maior que zero")
    return {"nome": nome, "area_ha": area_ha, "cultura": cultura}


if __name__ == "__main__":
    print(cadastrar_talhao("Talhao 01", 35.5, "Soja"))
