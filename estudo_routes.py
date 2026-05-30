from flask import Blueprint, request, jsonify
# ANTES: from services.gemini_service import gerar_conteudo
from gemini_service import gerar_conteudo  # AGORA: Importa direto da raiz

estudo_bp = Blueprint("estudo", __name__)

@estudo_bp.route("/gerarestudo", methods=["POST"])
def gerar_estudo():
    dados = request.json
    
    if not dados or "tema" not in dados:
        return jsonify({"erro": "O campo 'tema' é obrigatório no corpo da requisição."}), 400
        
    tema = dados.get("tema")
    resultado = gerar_conteudo(tema)
    
    return jsonify(resultado)