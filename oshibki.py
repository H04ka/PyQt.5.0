from PyQt5 import QtWidgets
import form


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = form.Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.pusto)
        self.ui.pushButton_2.clicked.connect(self.exit)
        self.ui.pushButton_3.clicked.connect(self.avtor)

    def pusto(self):
        if self.ui.lineEdit.text() == "":
            p = QtWidgets.QMessageBox.information(window, "Текст заголовка", "Текст сообщения",
                                                  buttons=QtWidgets.QMessageBox.Ok,
                                                  defaultButton=QtWidgets.QMessageBox.NoButton)
        
    
        if self.ui.lineEdit.text() == "#":
            sha = QtWidgets.QMessageBox.warning(window, "Текст заголовка", "Действие может быть опасным.Продолжим?",
                                                buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                                defaultButton=QtWidgets.QMessageBox.No)
            if sha == QtWidgets.QMessageBox.Yes:
                self.ui.label_2.setText("#")
            elif sha ==QtWidgets.QMessageBox.No:
                self.ui.label_2.setText(self.clear)
    
        if self.ui.lineEdit.text() == "666":
            krit = QtWidgets.QMessageBox.critical(window, "Текст заголовка", "Программа выполнила недопустимую ошибку и будет закрыта",
                                                  buttons=QtWidgets.QMessageBox.Ok,
                                                  defaultButton=QtWidgets.QMessageBox.NoButton)
            if krit == QtWidgets.QMessageBox.Ok:
                sys.exit(app.quit)
    def avtor(self):
        inf = QtWidgets.QMessageBox.about(window, "О программе", "\nMe\nBy Гайсин E.A \nContact: tg:@H0_04ka")
                                                


    def exit(self):
        ex = QtWidgets.QMessageBox.question(window,"Текст заголовка", "Вы действительно хотите совершить действие",
                                            buttons=QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No,
                                            defaultButton=QtWidgets.QMessageBox.Yes)
        if ex == QtWidgets.QMessageBox.Yes:
            sys.exit(app.quit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())