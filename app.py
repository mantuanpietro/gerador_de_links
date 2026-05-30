import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# IMPORTAÇÃO DA ROTA
from estudo_routes import estudo_bp

load_dotenv()

app = Flask(__name__)
CORS(app)

# REGISTRO DO BLUEPRINT
app.register_blueprint(estudo_bp)

@app.route("/")
def home():
    return {
        "mensagem": "API ROTA 27 funcionando"
    }

if __name__ == "__main__":
    app.run(debug=True)