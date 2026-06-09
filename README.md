# Ninja ChatBot 🍥

Um chatbot estilizado com tema Naruto, desenvolvido em Python com Flask e Google Gemini AI.

## 📁 Estrutura do Projeto

```
chatBotPython/
├── .env                    # Variáveis de ambiente (não versionado)
├── .env.example            # Exemplo de variáveis de ambiente
├── LICENSE                 # Licença do projeto
├── README.md               # Este arquivo
├── requirements.txt        # Dependências Python
└── src/
    └── chatbot/
        ├── __init__.py     # Inicializador do pacote
        ├── app.py          # Aplicação Flask principal
        ├── templates/      # Templates HTML (convenção Flask)
        │   └── index.html  # Interface do chatbot
        └── static/         # Arquivos estáticos
            ├── css/        # Estilos CSS
            └── js/         # Scripts JavaScript
```

## 🚀 Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure as variáveis de ambiente:
   ```bash
   cp .env.example .env
   # Edite .env e adicione sua GOOGLE_API_KEY
   ```

## ▶️ Execução

```bash
cd src/chatbot
python app.py
```

Acesse `http://localhost:5000` no navegador.

## 🔧 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | `/`      | Interface do chatbot |
| POST   | `/chat`  | Enviar mensagem |
| POST   | `/reset` | Reiniciar conversa |

## 🛠️ Tecnologias

- **Backend:** Python, Flask, Flask-CORS
- **AI:** Google Gemini 2.5 Flash
- **Frontend:** HTML, CSS, JavaScript vanilla
