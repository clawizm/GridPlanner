from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
import random
from PySide6.QtCore import Qt, Slot


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World",
                                     alignment=Qt.AlignCenter)

        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self.text)
        self._layout.addWidget(self.button)
        
        self.button.clicked.connect(self.magic)

    Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))    

if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()


