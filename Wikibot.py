import sys
from chat import agent
from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtGui import QFont, QColor, QTextCursor

# Main Window
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wikipedia Bot")
        self.setGeometry(500, 300, 600, 400)

        # Create widgets
        self.input_edit = QLineEdit()
        self.output_edit = QTextEdit()
        self.send_button = QPushButton("Send")

        # Configure widgets
        self.output_edit.setReadOnly(True)
        self.send_button.setDefault(True)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.output_edit)
        layout.addWidget(self.input_edit)
        layout.addWidget(self.send_button)

        # Set layout
        self.setLayout(layout)

        # Connect signals
        self.send_button.clicked.connect(self.send_message)
        self.input_edit.returnPressed.connect(self.send_message)

        #Initial Bot Message
        self.output_edit.setTextColor(QColor('#006600'))  # midnight blue
        self.output_edit.setFont(QFont('Courier', 12))
        self.output_edit.insertPlainText("Hello! I am Wikipedia Bot. How can I help?")


    def send_message(self):
        message = self.input_edit.text()
        self.input_edit.clear()

        # Display user input
        user_input = f'<br><p style="font-family: Courier; font-size: 11pt; color: black;">{message}</p><br>'
        self.output_edit.insertHtml(user_input)
        self.output_edit.moveCursor(QTextCursor.MoveOperation.EndOfBlock)

        #Display bot response
        response = agent(message)
        self.output_edit.setTextColor(QColor('#006600'))  # Midnight Blue
        self.output_edit.setFont(QFont('Courier', 12))
        self.output_edit.insertPlainText(response)
        self.output_edit.moveCursor(QTextCursor.MoveOperation.EndOfBlock)


def main():
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()