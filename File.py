import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

class Ui_Dialog(QMainWindow):
    def __init__(self):
        super().__init__()
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.setFixedSize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("QDialog{background-color:rgb(245, 121, 0);border:10px double black;}")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.filterbtn = QtWidgets.QPushButton(Dialog)
        self.filterbtn.setGeometry(QtCore.QRect(212, 360, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filterbtn.setFont(font)
        self.filterbtn.setStyleSheet("QPushButton{color:red;background-color:none;}")
        self.filterbtn.setObjectName("filterbtn")
        self.cancelbtn = QtWidgets.QPushButton(Dialog)
        self.cancelbtn.setGeometry(QtCore.QRect(300, 360, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cancelbtn.setFont(font)
        self.cancelbtn.setStyleSheet("QPushButton{color:red;background-color:none;}")
        self.cancelbtn.setObjectName("cancelbtn")
        self.path = QtWidgets.QLineEdit(Dialog)
        self.path.setGeometry(QtCore.QRect(30, 140, 221, 27))
        self.path.setObjectName("path")
        self.browserbtn = QtWidgets.QPushButton(Dialog)
        self.browserbtn.setGeometry(QtCore.QRect(270, 140, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.browserbtn.setFont(font)
        self.browserbtn.setStyleSheet("QPushButton{color:red;}")
        self.browserbtn.setObjectName("browserbtn")
        self.enterthepath = QtWidgets.QLabel(Dialog)
        self.enterthepath.setGeometry(QtCore.QRect(3, 110, 251, 27))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enterthepath.setFont(font)
        self.enterthepath.setStyleSheet("")
        self.enterthepath.setObjectName("enterthepath")
        self.link = QtWidgets.QLabel(Dialog)
        self.link.setGeometry(QtCore.QRect(65, 30, 340, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(70)
        self.link.setFont(font)
        self.link.setStyleSheet("QLabel{color:blue;}")
        self.link.setObjectName("link")
        self.contactme = QtWidgets.QLabel(Dialog)
        self.contactme.setGeometry(QtCore.QRect(15, 10, 200, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.contactme.setFont(font)
        self.contactme.setObjectName("contactme")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.working(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "File Separator According to Extension"))
        self.filterbtn.setText(_translate("Dialog", "Filter"))
        self.cancelbtn.setText(_translate("Dialog", "Close"))
        self.browserbtn.setText(_translate("Dialog", "Browser"))
        self.enterthepath.setText(_translate("Dialog", "     Enter The Path "))
        self.link.setText(_translate("Dialog", "https://m.facebook.com/Programmer404.py"))
        self.contactme.setText(_translate("Dialog", "-: Contact me on Facebook :- "))

    def working(self, Dialog):
        self.cancelbtn.clicked.connect(self.close)
        self.browserbtn.clicked.connect(self.browser)
        self.filterbtn.clicked.connect(self.sep)

    def close(self):
        sys.exit()

    def browser(self):
        self.dir_path = QFileDialog.getExistingDirectory(self, "Choose Directory", "E:\\")
        self.path.setText(self.dir_path)

    def sep(self):
        import os, shutil
        filterpath = self.path.text()
        os.chdir(filterpath)
        ext = []
        for i in os.listdir():
            ext.append(i[::-1].split('.')[0][::-1])
        ext = list(set(ext))
        for i in ext:
            if os.path.exists(i) == False:
                os.mkdir(i)
        for i in os.listdir():
            shutil.move(i, i[::-1].split('.')[0][::-1])

        self.path.setText("")
        msg = QMessageBox()
        msg.setWindowTitle("Message")
        msg.setText("Files are Separated Sucessfully")
        msg.exec_()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec_())
