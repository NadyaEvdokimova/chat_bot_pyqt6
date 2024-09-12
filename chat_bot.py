import cohere


class Chatbot:
    def __init__(self):
        self.co = cohere.Client(api_key='MmY9n02MMxD5PRRgDflqMvRUQTms26Uqb06X9JL7')

    def get_response(self, user_message):
        response = self.co.chat(
            model='command-r-plus',
            message=user_message
        )
        return response.text
