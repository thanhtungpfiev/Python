#VERSION2: Setting up a separate class
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Our first MainWindow App!")

        button = QPushButton()
        button.setText("Press Me")

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()

