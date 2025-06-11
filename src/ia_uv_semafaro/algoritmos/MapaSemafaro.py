COR_PARA_FORMA = {
    "VERMELHO": "Círculo",
    "AMARELO": "Triângulo",
    "VERDE": "Quadrado"
}

FORMA_PARA_COR = {v: k for k, v in COR_PARA_FORMA.items()}

def cor_para_forma(cor: str) -> str:
    return COR_PARA_FORMA.get(cor.upper(), "Desconhecida")

def forma_para_cor(forma: str) -> str:
    return FORMA_PARA_COR.get(forma.capitalize(), "Desconhecida")
