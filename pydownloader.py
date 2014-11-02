from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        self.download = QPushButton("Download")
        browser = QPushButton("Local")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("Local para salvar")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browser)
        layout.addWidget(self.progress)
        layout.addWidget(self.download)

        self.setLayout(layout)
        self.setWindowTitle("Sis PyDownloader")
        self.setFocus()

        self.download.clicked.connect(self.downloader)
        browser.clicked.connect(self.browser_file)

    def browser_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption="Salvar Como",directory=".",
                                                filter="Todos Arquivos(*.*)"  )
        self.save_location.setText(QDir.toNativeSeparators(save_file));


    def downloader(self):
        url = self.url.text()
        save_location = self.save_location.text()
        try:
            urllib.request.urlretrieve(url,save_location,self.report)
        except Exception:
            QMessageBox.warning(self,"Informação","Houve um erro!")
            return

        QMessageBox.information(self,"Informação","Download Concluido!")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report(self,blocknum,blocksize,totalsize):
        readsofar = blocknum * blocksize
        if totalsize>0:
            percent = readsofar *100 /totalsize
            self.progress.setValue(int(percent))



app = QApplication(sys.argv)
dl  = Downloader()
dl.show()
app.exec_()