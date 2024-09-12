import cohere
import os

class Chatbot:
    def __init__(self):
        self.co = cohere.Client(api_key=os.environ.get("API_KEY"))

    def get_response(self, user_message):
        response = self.co.chat(
            model='command-r-plus',
            message=user_message
        )
        return response.text
