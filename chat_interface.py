from app.chatbot import chat_response

def main():
    print("Olá! Eu sou um chatbot. Digite 'sair' para encerrar a conversa.")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            print("Chatbot: Até mais!")
            break
        
        response = chat_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
