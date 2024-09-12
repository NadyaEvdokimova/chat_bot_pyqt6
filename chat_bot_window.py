from PyQt6.QtWidgets import QMainWindow, QTextEdit, QPushButton
from PyQt6.QtCore import Qt

from chat_bot import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chat_bot = Chatbot()
        self.setMinimumSize(700, 500)
        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QTextEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.installEventFilter(self)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def eventFilter(self, source, event):
        if event.type() == event.Type.KeyPress and source is self.input_field:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter) and self.input_field.hasFocus():
                self.send_message()
                return True
        return super().eventFilter(source, event)

    def send_message(self):
        user_input = self.input_field.toPlainText().strip()
        if user_input:
            self.chat_area.append(f"<p style='color:#333333'><span style='color:#3443EA'>Me:</span> {user_input}</p>")
            self.input_field.clear()
            thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
            thread.start()

    def get_bot_response(self, user_input):
        bot_response = self.chat_bot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#3B3F8E; background-color: #E9E9E9'> Chat Bot: {bot_response}</p>")
