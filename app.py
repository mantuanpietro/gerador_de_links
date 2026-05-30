import os
from flask import Flask, render_template_string
from flask_cors import CORS
from dotenv import load_dotenv
from estudo_routes import estudo_bp

load_dotenv()

app = Flask(__name__)
# Permitir que qualquer frontend (Vercel, Localhost, etc.) consuma esta API sem bloqueios de CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Registrar todas as rotas inteligentes sob o blueprint
app.register_blueprint(estudo_bp)


# --- ROTA DE DOCUMENTAÇÃO NATIVA (SCALAR / OPENAPI) ---
@app.route("/docs")
def documentacao():
    # Renderiza uma interface interativa espetacular baseada na especificação OpenAPI (Swagger)
    return render_template_string("""
    <!doctype html>
    <html>
      <head>
        <title>ROTA 27 - API Docs</title>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style>
          body { margin: 0; }
        </style>
      </head>
      <body>
        <script
          id="api-reference"
          data-configuration='{
            "spec": {
              "openapi": "3.0.0",
              "info": {
                "title": "ROTA 27 - API de Estudos Inteligentes",
                "version": "1.0.0",
                "description": "Documentação interativa das rotas de Inteligência Artificial com Gemini para a ROTA 27."
              },
              "paths": {
                "/gerarestudo": {
                  "post": {
                    "summary": "Gerar Conteúdo de Estudo",
                    "description": "Retorna uma aula completa estruturada em JSON (Introdução, Tópicos, Curiosidades e Resumo).",
                    "requestBody": {
                      "required": true,
                      "content": {
                        "application/json": {
                          "schema": {
                            "type": "object",
                            "properties": { "tema": { "type": "string", "example": "Relevo de Portugal" } },
                            "required": ["tema"]
                          }
                        }
                      }
                    },
                    "responses": { "200": { "description": "Sucesso" } }
                  }
                },
                "/gerarflashcards": {
                  "post": {
                    "summary": "Gerar Flashcards",
                    "description": "Retorna exatamente 10 flashcards no formato JSON com chaves frente/verso.",
                    "requestBody": {
                      "required": true,
                      "content": {
                        "application/json": {
                          "schema": {
                            "type": "object",
                            "properties": { "tema": { "type": "string", "example": "Globalização" } },
                            "required": ["tema"]
                          }
                        }
                      }
                    },
                    "responses": { "200": { "description": "Sucesso" } }
                  }
                },
                "/gerarquiz": {
                  "post": {
                    "summary": "Gerar Quiz de Revisão",
                    "description": "Retorna 5 perguntas de múltipla escolha com opções de A a D e a resposta comentada.",
                    "requestBody": {
                      "required": true,
                      "content": {
                        "application/json": {
                          "schema": {
                            "type": "object",
                            "properties": { "tema": { "type": "string", "example": "Climas da Terra" } },
                            "required": ["tema"]
                          }
                        }
                      }
                    },
                    "responses": { "200": { "description": "Sucesso" } }
                  }
                },
                "/gerarmapas": {
                  "post": {
                    "summary": "Gerar Sugestões de Mapas e Mídias",
                    "description": "Retorna os melhores termos de pesquisa e fontes para encontrar mapas e infográficos.",
                    "requestBody": {
                      "required": true,
                      "content": {
                        "application/json": {
                          "schema": {
                            "type": "object",
                            "properties": { "tema": { "type": "string", "example": "Hidrografia de Portugal" } },
                            "required": ["tema"]
                          }
                        }
                      }
                    },
                    "responses": { "200": { "description": "Sucesso" } }
                  }
                },
                "/gerarvideos": {
                  "post": {
                    "summary": "Gerar Links e Canais de Vídeo",
                    "description": "Retorna termos de busca e canais recomendados no YouTube para o tema enviado.",
                    "requestBody": {
                      "required": true,
                      "content": {
                        "application/json": {
                          "schema": {
                            "type": "object",
                            "properties": { "tema": { "type": "string", "example": "Placas Tectónicas" } },
                            "required": ["tema"]
                          }
                        }
                      }
                    },
                    "responses": { "200": { "description": "Sucesso" } }
                  }
                }
              }
            },
            "theme": "purple"
          }'></script>
        <script src="https://cdn.jsdelivr.net/npm/@scalar/api-reference"></script>
      </body>
    </html>
    """)
# ------------------------------------------------------


@app.route("/")
def home():
    return {
        "sistema": "ROTA 27 - Estudos Inteligentes",
        "status": "online",
        "documentacao": "Aceda a /docs para ver a documentação interativa.",
        "endpoints": [
            "/gerarestudo",
            "/gerarflashcards",
            "/gerarquiz",
            "/gerarmapas",
            "/gerarvideos"
        ]
    }

if __name__ == "__main__":
    # Carrega a porta da variável de ambiente ou usa a 5000 por padrão
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta, debug=True)