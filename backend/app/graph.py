campus_graph = {
    "Entrada Frontal": {
        "Hall 1": {"distancia": 5, "direcao": "frente"}
    },
    "Entrada Traseira": {
        "Hall 1": {"distancia": 7, "direcao": "frente"}
    },

    "Hall 1": {
        "Entrada Frontal": {"distancia": 5, "direcao": "atrás"},
        "Entrada Traseira": {"distancia": 7, "direcao": "atrás"},
        "Corredor 1A": {"distancia": 4, "direcao": "esquerda"},
        "Corredor 1B": {"distancia": 4, "direcao": "direita"},
        "Escada 1": {"distancia": 3, "direcao": "frente"},
        "Escada 2": {"distancia": 3, "direcao": "frente"},
        "Rampa": {"distancia": 6, "direcao": "frente"}
    },

    "Corredor 1A": {
        "Hall 1": {"distancia": 4, "direcao": "direita"},
        "Sala 102": {"distancia": 3, "direcao": "esquerda"},
        "Sala 104": {"distancia": 3, "direcao": "frente"},
        "Sala 106": {"distancia": 3, "direcao": "frente"},
        "Banheiro 1A": {"distancia": 2, "direcao": "fim do corredor"}
    },
    "Corredor 1B": {
        "Hall 1": {"distancia": 4, "direcao": "esquerda"},
        "Sala 101": {"distancia": 3, "direcao": "direita"},
        "Sala 103": {"distancia": 3, "direcao": "frente"},
        "Sala 105": {"distancia": 3, "direcao": "frente"},
        "Banheiro 1B": {"distancia": 2, "direcao": "fim do corredor"}
    },

    "Sala 101": {"Corredor 1B": {"distancia": 3, "direcao": "esquerda"}},
    "Sala 102": {"Corredor 1A": {"distancia": 3, "direcao": "direita"}},
    "Sala 103": {"Corredor 1B": {"distancia": 3, "direcao": "atrás"}},
    "Sala 104": {"Corredor 1A": {"distancia": 3, "direcao": "atrás"}},
    "Sala 105": {"Corredor 1B": {"distancia": 3, "direcao": "atrás"}},
    "Sala 106": {"Corredor 1A": {"distancia": 3, "direcao": "atrás"}},
    "Banheiro 1A": {"Corredor 1A": {"distancia": 2, "direcao": "volte"}},
    "Banheiro 1B": {"Corredor 1B": {"distancia": 2, "direcao": "volte"}},

    "Escada 1": {
        "Hall 1": {"distancia": 3, "direcao": "atrás"},
        "Hall 2": {"distancia": 3, "direcao": "sobe"},
        "Hall 3": {"distancia": 3, "direcao": "sobe"}
    },
    "Escada 2": {
        "Hall 1": {"distancia": 3, "direcao": "atrás"},
        "Hall 2": {"distancia": 3, "direcao": "sobe"},
        "Hall 3": {"distancia": 3, "direcao": "sobe"}
    },
    "Rampa": {
        "Hall 1": {"distancia": 6, "direcao": "atrás"},
        "Hall 2": {"distancia": 6, "direcao": "sobe"},
        "Hall 3": {"distancia": 6, "direcao": "sobe"}
    },

    "Hall 2": {
        "Escada 1": {"distancia": 3, "direcao": "desce"},
        "Escada 2": {"distancia": 3, "direcao": "desce"},
        "Rampa": {"distancia": 6, "direcao": "desce"},
        "Corredor 2A": {"distancia": 4, "direcao": "esquerda"},
        "Corredor 2B": {"distancia": 4, "direcao": "direita"},
        "Lanchonete": {"distancia": 4, "direcao": "frente"}
    },

    "Corredor 2A": {
        "Hall 2": {"distancia": 4, "direcao": "direita"},
        "Sala 202": {"distancia": 3, "direcao": "esquerda"},
        "Sala 204": {"distancia": 3, "direcao": "frente"},
        "Sala 206": {"distancia": 3, "direcao": "frente"},
        "Banheiro 2A": {"distancia": 2, "direcao": "fim do corredor"}
    },
    "Corredor 2B": {
        "Hall 2": {"distancia": 4, "direcao": "esquerda"},
        "Sala 201": {"distancia": 3, "direcao": "direita"},
        "Sala 203": {"distancia": 3, "direcao": "frente"},
        "Sala 205": {"distancia": 3, "direcao": "frente"},
        "Banheiro 2B": {"distancia": 2, "direcao": "fim do corredor"}
    },

    "Sala 201": {"Corredor 2B": {"distancia": 3, "direcao": "esquerda"}},
    "Sala 202": {"Corredor 2A": {"distancia": 3, "direcao": "direita"}},
    "Sala 203": {"Corredor 2B": {"distancia": 3, "direcao": "atrás"}},
    "Sala 204": {"Corredor 2A": {"distancia": 3, "direcao": "atrás"}},
    "Sala 205": {"Corredor 2B": {"distancia": 3, "direcao": "atrás"}},
    "Sala 206": {"Corredor 2A": {"distancia": 3, "direcao": "atrás"}},
    "Banheiro 2A": {"Corredor 2A": {"distancia": 2, "direcao": "volte"}},
    "Banheiro 2B": {"Corredor 2B": {"distancia": 2, "direcao": "volte"}},
    "Lanchonete": {"Hall 2": {"distancia": 4, "direcao": "atrás"}},

    "Hall 3": {
        "Escada 1": {"distancia": 3, "direcao": "desce"},
        "Escada 2": {"distancia": 3, "direcao": "desce"},
        "Rampa": {"distancia": 6, "direcao": "desce"},
        "Corredor 3A": {"distancia": 4, "direcao": "esquerda"},
        "Corredor 3B": {"distancia": 4, "direcao": "direita"},
        "Web Class": {"distancia": 4, "direcao": "frente"}
    },

    "Corredor 3A": {
        "Hall 3": {"distancia": 4, "direcao": "direita"},
        "Sala 302": {"distancia": 3, "direcao": "esquerda"},
        "Sala 304": {"distancia": 3, "direcao": "frente"},
        "Sala 306": {"distancia": 3, "direcao": "frente"},
        "Banheiro 3A": {"distancia": 2, "direcao": "fim do corredor"}
    },
    "Corredor 3B": {
        "Hall 3": {"distancia": 4, "direcao": "esquerda"},
        "Sala 301": {"distancia": 3, "direcao": "direita"},
        "Sala 303": {"distancia": 3, "direcao": "frente"},
        "Sala 305": {"distancia": 3, "direcao": "frente"},
        "Banheiro 3B": {"distancia": 2, "direcao": "fim do corredor"}
    },

    "Sala 301": {"Corredor 3B": {"distancia": 3, "direcao": "esquerda"}},
    "Sala 302": {"Corredor 3A": {"distancia": 3, "direcao": "direita"}},
    "Sala 303": {"Corredor 3B": {"distancia": 3, "direcao": "atrás"}},
    "Sala 304": {"Corredor 3A": {"distancia": 3, "direcao": "atrás"}},
    "Sala 305": {"Corredor 3B": {"distancia": 3, "direcao": "atrás"}},
    "Sala 306": {"Corredor 3A": {"distancia": 3, "direcao": "atrás"}},
    "Banheiro 3A": {"Corredor 3A": {"distancia": 2, "direcao": "volte"}},
    "Banheiro 3B": {"Corredor 3B": {"distancia": 2, "direcao": "volte"}},
    "Web Class": {"Hall 3": {"distancia": 4, "direcao": "atrás"}}
}
