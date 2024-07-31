import sys
import os

# Adicionar o diretório raiz ao caminho de importação
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from data.preprocess import preprocess_text, load_intents  # Usando 'data'

# Carregar e preprocessar os dados
intents = load_intents('data/intents.json')  # Usando 'data'
# (Adicionar código para converter intents em dados de treinamento)

training_data = []
training_labels = []
all_words = []
tags = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = preprocess_text(pattern)
        all_words.extend(word_list)
        training_data.append(word_list)
        training_labels.append(intent['tag'])
    
    if intent['tag'] not in tags:
        tags.append(intent['tag'])

all_words = sorted(set(all_words))
tags = sorted(set(tags))

training_X = []
training_y = []

for (pattern_sentence, tag) in zip(training_data, training_labels):
    bag = [1 if word in pattern_sentence else 0 for word in all_words]
    training_X.append(bag)
    label = tags.index(tag)
    training_y.append(label)

training_X = np.array(training_X)
training_y = np.array(training_y)

model = Sequential([
    Dense(128, input_shape=(len(training_X[0]),), activation='relu'),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(len(tags), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(training_X, training_y, epochs=200, batch_size=8, verbose=1)
model.save('models/chatbot_model.h5')  # Usando 'models'
