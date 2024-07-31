# Chatbot com TensorFlow

Este é um projeto de chatbot que usa TensorFlow e NLTK para criar um bot que pode aprender com as interações do usuário.

## Estrutura do Projeto
```
chatbot/
│
├── data/
│ ├── intents.json # Arquivo JSON com exemplos de intenções e respostas
│ └── preprocess.py # Script para preprocessar dados
│
├── models/
│ └── chatbot_model.h5 # Arquivo de modelo treinado
│
├── app/
│ ├── init.py # Inicialização do módulo
│ ├── chatbot.py # Lógica do chatbot
│ ├── training.py # Script para treinar o modelo
│ └── update_model.py # Script para atualizar o modelo
│
├── web/
│ ├── init.py # Inicialização do módulo
│ └── app.py # Aplicação Flask para interface web
│
├── tests/
│ ├── test_chatbot.py # Testes para a lógica do chatbot
│ └── test_training.py # Testes para o treinamento do modelo
│
├── venv/ # Ambiente virtual
│
├── requirements.txt # Arquivo de dependências
└── README.md # Documentação do projeto
```

## Configuração do Ambiente

1. Clone o repositório:
    ```bash
    git clone https://github.com/username/chatbot.git
    cd chatbot
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Baixe os pacotes NLTK necessários:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

5. Treine o modelo:
    ```bash
    python app/training.py
    ```

6. Execute a aplicação Flask:
    ```bash
    python web/app.py
    ```

## Testes

Para executar os testes, use:
```bash
python -m unittest discover testes
```

## Executar interação pelo prompt:

````bash
python chat_interface.py
```

## Executar interação pelo Web com Flask:

````bash
python web/app.py
```
