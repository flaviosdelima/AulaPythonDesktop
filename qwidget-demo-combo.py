from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidget Demos")

        self.combobox1 = QComboBox()
        self.combobox1.addItems(["Item 1","Item 2","Item 3"])
        #self.combobox1.addItem("Item 1")
        #self.combobox1.addItem("Item 2")
       # self.combobox1.addItem("Item 3")
       # self.combobox1.addItem("Item 4")

        close_button = QPushButton("Fechar")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(close_button)
        layout.addWidget(self.combobox1)
        self.setLayout(layout)

        self.setFocus()

        self.combobox1.currentIndexChanged.connect(self.selecionado)

    def selecionado(self):
        current_text = self.combobox1.currentText()
        current_index = str(self.combobox1.currentIndex())
        print(current_text+" Em  "+ current_index)


app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()