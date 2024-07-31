from tensorflow.keras.models import load_model
from app.training import train_model

model = load_model('models/chatbot_model.h5')  # Atualizado para usar 'models'

def update_model(new_data, new_labels):
    # Adicione novos dados ao conjunto de treinamento e treine novamente
    train_model(new_data, new_labels)
    model.save('models/chatbot_model_updated.h5')  # Atualizado para usar 'models'
