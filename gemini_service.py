import os
import google.generativeai as genai

# Importações corrigidas apontando para as pastas corretas da estrutura
from prompts.geography_prompts import PROMPT_GEOGRAFIA
from utils.formatter import formatar_resposta

# Configura a API utilizando a variável de ambiente do .env
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def gerar_conteudo(tema):
    if not os.getenv("GEMINI_API_KEY"):
        return {"sucesso": False, "erro": "Chave API do Gemini não configurada no servidor."}

    try:
        # Utilizando o modelo flash para respostas textuais rápidas
        model = genai.GenerativeModel('gemini-3.5-flash')
        
        # Concatena as instruções do professor com o tema solicitado
        prompt_final = f"{PROMPT_GEOGRAFIA}\n\nExplique o seguinte tema para alunos do fundamental II: {tema}"
        
        resposta = model.generate_content(prompt_final)
        texto_formatado = formatar_resposta(resposta.text)
        
        return {
            "sucesso": True,
            "tema": tema,
            "conteudo": texto_formatado
        }
        
    except Exception as e:
        return {
            "sucesso": False,
            "erro": str(e)
        }