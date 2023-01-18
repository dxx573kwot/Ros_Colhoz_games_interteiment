import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.name_input = QLineEdit(self)
        self.name_input.move(100, 20)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.name_input1 = QLineEdit(self)
        self.name_input1.move(100, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.name_input2 = QLineEdit(self)
        self.name_input2.move(100, 80)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.name_input3 = QLineEdit(self)
        self.name_input3.move(100, 110)

        cb1 = QCheckBox('Show title', self)
        cb1.move(20, 50)
        cb1.toggle()
        cb1.stateChanged.connect(self.changeTitle1)

        cb2 = QCheckBox('Show title', self)
        cb2.move(20, 80)
        cb2.toggle()
        cb2.stateChanged.connect(self.changeTitle2)

        cb3 = QCheckBox('Show title', self)
        cb3.move(20, 110)
        cb3.toggle()
        cb3.stateChanged.connect(self.changeTitle3)


        self.show()


    def changeTitle(self, state):

        if state == Qt.Checked:
            QWidget.show(self.name_input)
        else:
            QWidget.hide(self.name_input)

    def changeTitle1(self, state):

        if state == Qt.Checked:
            QWidget.show(self.name_input1)
        else:
            QWidget.hide(self.name_input1)

    def changeTitle2(self, state):

        if state == Qt.Checked:
            QWidget.show(self.name_input2)
        else:
            QWidget.hide(self.name_input2)

    def changeTitle3(self, state):

        if state == Qt.Checked:
            QWidget.show(self.name_input3)
        else:
            QWidget.hide(self.name_input3)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
