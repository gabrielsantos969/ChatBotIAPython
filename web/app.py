from flask import Flask, request, jsonify
from app.chatbot import chat_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('mensagem')
    response = chat_response(user_message)
    return jsonify({"resposta": response})

if __name__ == "__main__":
    app.run(debug=True)
