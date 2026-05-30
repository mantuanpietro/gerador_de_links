import os
import json
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)

def _chamar_gemini_json(prompt):
    """Função interna auxiliar para garantir e tratar o retorno JSON do Gemini."""
    if not api_key:
        return {"sucesso": False, "erro": "Chave API do Gemini não configurada."}
    try:
        # Forçamos o modelo a focar em respostas JSON estruturadas
        model = genai.GenerativeModel("gemini-2.5-flash")
        resposta = model.generate_content(prompt)
        
        texto = resposta.text.strip()
        # Limpeza agressiva de blocos de código Markdown gerados acidentalmente
        if texto.startswith("```"):
            lines = texto.splitlines()
            if lines[0].startswith("```"):
                lines = lines[1:]
            if lines[-1].startswith("```"):
                lines = lines[:-1]
            texto = "\n".join(lines).strip()
            
        dados = json.loads(texto)
        return {"sucesso": True, "dados": dados}
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}

def gerar_conteudo_estudo(tema):
    prompt = f"""
    Atue como a professora Jesiane, especialista em Geografia para o Ensino Fundamental II (11 a 15 anos).
    Gere um plano de estudos super didático sobre o tema "{tema}".
    O retorno deve ser estritamente em formato JSON, obedecendo a seguinte estrutura:
    {{
        "tema": "{tema}",
        "introducao": "Texto simples e contextualizado com emojis.",
        "explicacao_topicos": [
            {{"titulo": "Nome do Tópico", "conteudo": "Explicação em tópicos com exemplos cotidianos."}}
        ],
        "curiosidades": ["Curiosidade 1", "Curiosidade 2"],
        "resumo": "Breve resumo com os pontos mais importantes para memorização."
    }}
    Responda apenas com o JSON. Não inclua markdown ```json ou explicações externas.
    """
    return _chamar_gemini_json(prompt)

def gerar_flashcards_service(tema):
    prompt = f"""
    Gere exatamente 10 flashcards de revisão sobre o tema de Geografia: "{tema}".
    Foco em alunos de 11 a 15 anos.
    O retorno deve ser estritamente em formato JSON, obedecendo a seguinte estrutura:
    {{
        "tema": "{tema}",
        "flashcards": [
            {{"frente": "Pergunta ou conceito chave direto", "verso": "Resposta clara, direta e objetiva"}}
        ]
    }}
    Responda apenas com o JSON. Não inclua markdown ```json ou explicações externas.
    """
    return _chamar_gemini_json(prompt)

def gerar_quiz_service(tema):
    prompt = f"""
    Gere exatamente 5 perguntas de múltipla escolha (Quiz) desafiadoras mas adequadas sobre o tema: "{tema}".
    O retorno deve ser estritamente em formato JSON, obedecendo a seguinte estrutura:
    {{
        "tema": "{tema}",
        "quiz": [
            {{
                "pergunta": "Enunciado da pergunta",
                "opcoes": {{
                    "A": "Texto da opção A",
                    "B": "Texto da opção B",
                    "C": "Texto da opção C",
                    "D": "Texto da opção D"
                }},
                "resposta_correta": "A",
                "explicacao": "Explicação curta do porquê esta alternativa está correta."
            }}
        ]
    }}
    Responda apenas com o JSON. Não inclua markdown ```json ou explicações externas.
    """
    return _chamar_gemini_json(prompt)

def gerar_midia_mapas_service(tema):
    prompt = f"""
    Você deve sugerir termos de busca altamente precisos e URLs conceituais para Mapas, Infográficos ou Imagens Reais sobre o tema "{tema}".
    Como o Gemini não navega em tempo real para validar links mutáveis, monte uma estrutura JSON com termos de busca ideais para o Google Imagens e sugestões estáveis (ex: Wikimedia Commons, IBGE).
    Estrutura do JSON:
    {{
        "tema": "{tema}",
        "midias": [
            {{
                "tipo": "Mapa Principal / Infográfico / Imagem Ilustrativa",
                "titulo": "Título descritivo da imagem",
                "termo_busca_google": "O termo exato que o aluno deve jogar no Google Imagens",
                "sugestao_fonte": "Ex: IBGE, NASA, Wikimedia"
            }}
        ]
    }}
    Gere pelo menos 3 mídias recomendadas. Responda apenas com o JSON.
    """
    return _chamar_gemini_json(prompt)

def gerar_videos_youtube_service(tema):
    prompt = f"""
    Atue como curador de conteúdo educativo de Geografia. Sugira títulos de vídeos e canais recomendados no YouTube para o tema "{tema}".
    Gere links de buscas prontos ou canais consolidados (Ex: Nostalgia Ciência, Manual do Mundo, Khan Academy, GeoBrasil).
    Estrutura do JSON:
    {{
        "tema": "{tema}",
        "videos_recomendados": [
            {{
                "titulo_sugerido": "Título provável do vídeo educativo",
                "canal": "Nome do canal recomendado",
                "url_busca_pronta": "https://www.youtube.com/results?search_query=termo+de+busca"
            }}
        ]
    }}
    Gere 3 recomendações. Responda apenas com o JSON.
    """
    return _chamar_gemini_json(prompt)