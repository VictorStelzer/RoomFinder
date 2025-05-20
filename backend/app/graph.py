campus_graph = {
    "EntradaFrontal": {
        "Hall1": {"distancia": 5, "direcao": "frente"}
    },
    "EntradaTraseira": {
        "Hall1": {"distancia": 7, "direcao": "frente"}
    },

    "Hall1": {
        "EntradaFrontal": {"distancia": 5, "direcao": "atrás"},
        "EntradaTraseira": {"distancia": 7, "direcao": "atrás"},
        "Corredor1A": {"distancia": 4, "direcao": "esquerda"},
        "Corredor1B": {"distancia": 4, "direcao": "direita"},
        "Escada1": {"distancia": 3, "direcao": "frente"},
        "Escada2": {"distancia": 3, "direcao": "frente"},
        "Rampa": {"distancia": 6, "direcao": "frente"}
    },

    "Corredor1A": {
        "Hall1": {"distancia": 4, "direcao": "direita"},
        "Sala102": {"distancia": 3, "direcao": "esquerda"},
        "Sala104": {"distancia": 3, "direcao": "frente"},
        "Sala106": {"distancia": 3, "direcao": "frente"},
        "Banheiro1A": {"distancia": 2, "direcao": "fim do corredor"}
    },
    "Corredor1B": {
        "Hall1": {"distancia": 4, "direcao": "esquerda"},
        "Sala101": {"distancia": 3, "direcao": "direita"},
        "Sala103": {"distancia": 3, "direcao": "frente"},
        "Sala105": {"distancia": 3, "direcao": "frente"},
        "Banheiro1B": {"distancia": 2, "direcao": "fim do corredor"}
    },

    "Sala101": {"Corredor1B": {"distancia": 3, "direcao": "esquerda"}},
    "Sala102": {"Corredor1A": {"distancia": 3, "direcao": "direita"}},
    "Sala103": {"Corredor1B": {"distancia": 3, "direcao": "atrás"}},
    "Sala104": {"Corredor1A": {"distancia": 3, "direcao": "atrás"}},
    "Sala105": {"Corredor1B": {"distancia": 3, "direcao": "atrás"}},
    "Sala106": {"Corredor1A": {"distancia": 3, "direcao": "atrás"}},
    "Banheiro1A": {"Corredor1A": {"distancia": 2, "direcao": "volte"}},
    "Banheiro1B": {"Corredor1B": {"distancia": 2, "direcao": "volte"}},

    "Escada1": {
        "Hall1": {"distancia": 3, "direcao": "atrás"},
        "Hall2": {"distancia": 3, "direcao": "sobe"},
        "Hall3": {"distancia": 3, "direcao": "sobe"}
    },
    "Escada2": {
        "Hall1": {"distancia": 3, "direcao": "atrás"},
        "Hall2": {"distancia": 3, "direcao": "sobe"},
        "Hall3": {"distancia": 3, "direcao": "sobe"}
    },
    "Rampa": {
        "Hall1": {"distancia": 6, "direcao": "atrás"},
        "Hall2": {"distancia": 6, "direcao": "sobe"},
        "Hall3": {"distancia": 6, "direcao": "sobe"}
    },

    "Hall2": {
        "Escada1": {"distancia": 3, "direcao": "desce"},
        "Escada2": {"distancia": 3, "direcao": "desce"},
        "Rampa": {"distancia": 6, "direcao": "desce"},
        "Corredor2A": {"distancia": 4, "direcao": "esquerda"},
        "Corredor2B": {"distancia": 4, "direcao": "direita"},
        "Lanchonete": {"distancia": 4, "direcao": "frente"}
    },

    "Corredor2A": {
        "Hall2": {"distancia": 4, "direcao": "direita"},
        "Sala202": {"distancia": 3, "direcao": "esquerda"},
        "Sala204": {"distancia": 3, "direcao": "frente"},
        "Sala206": {"distancia": 3, "direcao": "frente"},
        "Banheiro2A": {"distancia": 2, "direcao": "fim do corredor"}
    },
    "Corredor2B": {
        "Hall2": {"distancia": 4, "direcao": "esquerda"},
        "Sala201": {"distancia": 3, "direcao": "direita"},
        "Sala203": {"distancia": 3, "direcao": "frente"},
        "Sala205": {"distancia": 3, "direcao": "frente"},
        "Banheiro2B": {"distancia": 2, "direcao": "fim do corredor"}
    },

    "Sala201": {"Corredor2B": {"distancia": 3, "direcao": "esquerda"}},
    "Sala202": {"Corredor2A": {"distancia": 3, "direcao": "direita"}},
    "Sala203": {"Corredor2B": {"distancia": 3, "direcao": "atrás"}},
    "Sala204": {"Corredor2A": {"distancia": 3, "direcao": "atrás"}},
    "Sala205": {"Corredor2B": {"distancia": 3, "direcao": "atrás"}},
    "Sala206": {"Corredor2A": {"distancia": 3, "direcao": "atrás"}},
    "Banheiro2A": {"Corredor2A": {"distancia": 2, "direcao": "volte"}},
    "Banheiro2B": {"Corredor2B": {"distancia": 2, "direcao": "volte"}},
    "Lanchonete": {"Hall2": {"distancia": 4, "direcao": "atrás"}},

    "Hall3": {
        "Escada1": {"distancia": 3, "direcao": "desce"},
        "Escada2": {"distancia": 3, "direcao": "desce"},
        "Rampa": {"distancia": 6, "direcao": "desce"},
        "Corredor3A": {"distancia": 4, "direcao": "esquerda"},
        "Corredor3B": {"distancia": 4, "direcao": "direita"},
        "WebClass": {"distancia": 4, "direcao": "frente"}
    },

    "Corredor3A": {
        "Hall3": {"distancia": 4, "direcao": "direita"},
        "Sala302": {"distancia": 3, "direcao": "esquerda"},
        "Sala304": {"distancia": 3, "direcao": "frente"},
        "Sala306": {"distancia": 3, "direcao": "frente"},
        "Banheiro3A": {"distancia": 2, "direcao": "fim do corredor"}
    },
    "Corredor3B": {
        "Hall3": {"distancia": 4, "direcao": "esquerda"},
        "Sala301": {"distancia": 3, "direcao": "direita"},
        "Sala303": {"distancia": 3, "direcao": "frente"},
        "Sala305": {"distancia": 3, "direcao": "frente"},
        "Banheiro3B": {"distancia": 2, "direcao": "fim do corredor"}
    },

    "Sala301": {"Corredor3B": {"distancia": 3, "direcao": "esquerda"}},
    "Sala302": {"Corredor3A": {"distancia": 3, "direcao": "direita"}},
    "Sala303": {"Corredor3B": {"distancia": 3, "direcao": "atrás"}},
    "Sala304": {"Corredor3A": {"distancia": 3, "direcao": "atrás"}},
    "Sala305": {"Corredor3B": {"distancia": 3, "direcao": "atrás"}},
    "Sala306": {"Corredor3A": {"distancia": 3, "direcao": "atrás"}},
    "Banheiro3A": {"Corredor3A": {"distancia": 2, "direcao": "volte"}},
    "Banheiro3B": {"Corredor3B": {"distancia": 2, "direcao": "volte"}},
    "WebClass": {"Hall3": {"distancia": 4, "direcao": "atrás"}}
}
