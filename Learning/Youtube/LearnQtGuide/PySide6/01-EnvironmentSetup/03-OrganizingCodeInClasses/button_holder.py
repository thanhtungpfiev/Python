from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Our first MainWindow App!")

        button = QPushButton()
        button.setText("Press Me")

        self.setCentralWidget(button)