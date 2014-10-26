from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout = QGridLayout()
        self.label = QLabel("Olá Mundo!!")
        line_edit = QLineEdit()
        button = QPushButton("Fechar")

        layout.addWidget(self.label,0,0)
        layout.addWidget(line_edit,0,1)
        layout.addWidget(button,1,1)
        self.setLayout(layout)

        button.clicked.connect(self.close)
        #line_edit.textChanged.connect(label.setText)
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self,texto):
        self.label.setText(('Igreja - '+texto))

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()
