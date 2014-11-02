from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class QWidgetDemos(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("QWidget Demos")

        line_edit = QLineEdit()
        self.checkBox1 = QCheckBox()
        self.checkBox1.setText("Curso python")
        self.checkBox1.setChecked(True)
        label1 = QLabel()
        label1.setText("Curso de Python")
        #Da para escrever HTML dentro do label!!!
        label1.setText("<b>Curso de Python</b>")

        line_edit.setText("Hello Pluralsight")
        #line_edit.setEchoMode(QLineEdit.Password)
        #line_edit.selectAll()
        #line_edit.setReadOnly(True)
        #line_edit.setPlaceholderText("Hello Pluralsight")
        text = line_edit.text()
        print("Foi digitado "+text)
        print("Uma mensagem no console")

        close_button = QPushButton("Fechar")
        close_button.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(line_edit)
        layout.addWidget(close_button)
        layout.addWidget(label1)
        layout.addWidget(self.checkBox1)
        self.setLayout(layout)

        self.setFocus()

        self.checkBox1.stateChanged.connect(self.CheckBoxSelecionado)

    def CheckBoxSelecionado(self):
         if self.checkBox1.isChecked():
             print("Tá marcado")
         else:
             print("Não marcou")

app = QApplication(sys.argv)
dialog = QWidgetDemos()
dialog.show()
app.exec_()
