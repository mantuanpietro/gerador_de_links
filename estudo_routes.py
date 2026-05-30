from flask import Blueprint, request, jsonify
from gemini_service import (
    gerar_conteudo_estudo,
    gerar_flashcards_service,
    gerar_quiz_service,
    gerar_midia_mapas_service,
    gerar_videos_youtube_service
)

estudo_bp = Blueprint("estudo", __name__)

def validar_requisicao(dados):
    if not dados or "tema" not in dados:
        return False, jsonify({"erro": "O campo 'tema' é obrigatório no corpo da requisição."}), 400
    return True, dados.get("tema"), 200

@estudo_bp.route("/gerarestudo", methods=["POST"])
def rota_estudo():
    valido, resultado, status = validar_requisicao(request.json)
    if not valido: return resultado, status
    return jsonify(gerar_conteudo_estudo(resultado))

@estudo_bp.route("/gerarflashcards", methods=["POST"])
def rota_flashcards():
    valido, resultado, status = validar_requisicao(request.json)
    if not valido: return resultado, status
    return jsonify(gerar_flashcards_service(resultado))

@estudo_bp.route("/gerarquiz", methods=["POST"])
def rota_quiz():
    valido, resultado, status = validar_requisicao(request.json)
    if not valido: return resultado, status
    return jsonify(gerar_quiz_service(resultado))

@estudo_bp.route("/gerarmapas", methods=["POST"])
def rota_mapas():
    valido, resultado, status = validar_requisicao(request.json)
    if not valido: return resultado, status
    return jsonify(gerar_midia_mapas_service(resultado))

@estudo_bp.route("/gerarvideos", methods=["POST"])
def rota_videos():
    valido, resultado, status = validar_requisicao(request.json)
    if not valido: return resultado, status
    return jsonify(gerar_videos_youtube_service(resultado))