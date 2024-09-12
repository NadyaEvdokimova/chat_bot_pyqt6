import sys
from PyQt6.QtWidgets import QApplication
from chat_bot_window import ChatbotWindow


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
