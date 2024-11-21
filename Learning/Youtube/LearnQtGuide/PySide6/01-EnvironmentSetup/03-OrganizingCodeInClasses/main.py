#VERSION3: Setting up a separate class
from PySide6.QtWidgets import QApplication
import sys
from button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()

