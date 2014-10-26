from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()
        label = QLabel("Olá Mundo!!")
        line_edit = QLineEdit()
        button = QPushButton("Fechar")

        layout.addWidget(label)
        layout.addWidget(line_edit)
        layout.addWidget(button)
        self.setLayout(layout)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()
