def shape_to_color(shape: str) -> str:
    shape_map = {
       "VERMELHO": "Círculo",
        "AMARELO": "Triângulo",
        "VERDE": "Quadrado"
    }
    return shape_map.get(shape.lower(), 'DESCONHECIDO') 