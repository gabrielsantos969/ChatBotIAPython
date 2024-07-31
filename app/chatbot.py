import numpy as np
from tensorflow.keras.models import load_model
from data.preprocess import preprocess_text, load_intents
from datetime import datetime
import re

# Carregar dados e modelo
intents = load_intents('data/intents.json')
model = load_model('models/chatbot_model.h5')

# Variáveis globais
user_name = None
unknown_phrases = []  # Lista para registrar frases desconhecidas

def bag_of_words(text, all_words):
    """
    Cria uma representação de 'bag of words' para a frase de entrada.
    """
    tokens = preprocess_text(text)  # Obter tokens da entrada
    return np.array([1 if word in tokens else 0 for word in all_words])

def extract_name(text):
    """
    Extrai o nome do texto, se possível.
    """
    patterns = ["Meu nome é", "Eu me chamo", "Pode me chamar de", "Eu sou"]
    pattern = re.compile('|'.join(patterns) + r' (\w+)', re.IGNORECASE)
    match = pattern.search(text)
    return match.group(1) if match else None

def get_response(tag, text):
    """
    Retorna a resposta apropriada com base no tag do intent e o texto do usuário.
    """
    global user_name
    
    if tag == "pergunta_horario":
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"{user_name}, a hora atual é {current_time}." if user_name else f"A hora atual é {current_time}."
    
    if tag == "nome_usuario":
        name = extract_name(text)
        if name:
            user_name = name
            return f"Prazer em conhecê-lo, {user_name}!"
        else:
            return "Desculpe, não consegui pegar o seu nome. Pode repetir, por favor?"
    
    # Para outros intents, retorne uma resposta aleatória
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = np.random.choice(intent['responses'])
            return response.replace("{nome}", user_name if user_name else "amigo")

    return "Desculpe, não entendi o que você quis dizer. Pode reformular sua pergunta?"

def chat_response(text):
    """
    Gera uma resposta com base na entrada do usuário.
    """
    global unknown_phrases, user_name
    
    # Extraindo todas as palavras e tags dos intents
    all_words = sorted(set(word for intent in intents['intents'] for pattern in intent['patterns'] for word in preprocess_text(pattern)))
    tags = sorted(set(intent['tag'] for intent in intents['intents']))

    # Convertendo o texto do usuário para a forma que o modelo espera
    input_data = bag_of_words(text, all_words)
    input_data = input_data.reshape(1, -1)  # Ajustar para o formato esperado pelo modelo

    # Obter a previsão do modelo
    prediction = model.predict(input_data)
    predicted_tag = tags[np.argmax(prediction)]

    # Verificar se o texto corresponde a um intent conhecido
    intent_found = any(intent['tag'] == predicted_tag for intent in intents['intents'])

    # Obter a resposta baseada no intent previsto
    if intent_found:
        return get_response(predicted_tag, text)
    else:
        # Adicionar a frase desconhecida à lista de desconhecidos
        unknown_phrases.append(text)
        return "Desculpe, não entendi o que você quis dizer. Pode reformular sua pergunta?"

def greet_user():
    """
    Gera uma saudação para o usuário, usando o nome, se disponível.
    """
    global user_name
    return f"Olá novamente, {user_name}! Como posso ajudar você hoje?" if user_name else "Olá! Como posso ajudar você hoje?"

def show_unknown_phrases():
    """
    Exibe a lista de frases desconhecidas.
    """
    if unknown_phrases:
        return "Frases que eu ainda não sei responder:\n" + "\n".join(unknown_phrases)
    else:
        return "Ainda não há frases desconhecidas registradas."
