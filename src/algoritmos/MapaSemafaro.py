def shape_to_color(shape: str) -> str:
    shape_map = {
        'circle': 'VERMELHO',
        'triangle': 'AMARELO',
        'square': 'VERDE'
    }
    return shape_map.get(shape.lower(), 'DESCONHECIDO') 