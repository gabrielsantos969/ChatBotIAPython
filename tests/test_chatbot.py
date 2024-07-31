import unittest
from app.chatbot import chat_response

class ChatbotTestCase(unittest.TestCase):
    def test_saudacao(self):
        self.assertEqual(chat_response("Oi"), "Esta é uma resposta de exemplo.")

if __name__ == '__main__':
    unittest.main()
