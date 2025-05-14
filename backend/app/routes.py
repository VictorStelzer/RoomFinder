# routes.py
from flask import Blueprint, jsonify, request
from .dijkstra import dijkstra, get_valid_points
from .graph import campus_graph

bp = Blueprint('routes', __name__)

@bp.route('/')
def home():
    return jsonify({
        "mensagem": "Bem-vindo ao RoomFinder API!",
        "rotas_disponiveis": {
            "/pontos": "Lista todos os pontos disponíveis para navegação.",
            "/caminho?origem=X&destino=Y": "Retorna o menor caminho entre dois pontos."
        }
    })

@bp.route('/pontos', methods=['GET'])
def pontos():
    pontos_disponiveis = get_valid_points(campus_graph)
    return jsonify({"pontos_disponiveis": pontos_disponiveis})

@bp.route('/caminho', methods=['GET'])
def caminho():
    origem = request.args.get('origem')
    destino = request.args.get('destino')

    if not origem or not destino:
        return jsonify({"erro": "Parâmetros 'origem' e 'destino' são obrigatórios"}), 400

    caminho, distancia = dijkstra(campus_graph, origem, destino)

    if caminho:
        # Format the path with directions
        formatted_path = []
        for i, step in enumerate(caminho[:-1]):
            current_node, direction, distance = step
            next_node = caminho[i+1][0]
            if direction:
                formatted_path.append(f"{i+1}. Vá para {next_node} ({direction}, {distance}m)")
        
        return jsonify({
            "caminho_formatado": formatted_path,
            "distancia_total": f"{distancia} metros",
            "detalhes": {
                "caminho": caminho,
                "distancia": distancia
            }
        })
    else:
        return jsonify({"erro": "Caminho não encontrado"}), 404