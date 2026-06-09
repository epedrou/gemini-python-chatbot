import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    """Serve the main chat interface."""
    return render_template("index.html")

# Inicializa o cliente e o chat
client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")


@app.route("/chat", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    prompt = data.get("message", "")
    
    if not prompt:
        return jsonify({"error": "Mensagem vazia"}), 400
    
    try:
        resposta = chat.send_message(prompt)
        return jsonify({"response": resposta.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset", methods=["POST"])
def reset_chat():
    global chat
    chat = client.chats.create(model="gemini-2.5-flash")
    return jsonify({"message": "Chat reiniciado"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
