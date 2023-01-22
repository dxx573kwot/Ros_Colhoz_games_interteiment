import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать музыку', '', 'Музыка (*.wav)')[0]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    fname = ex.fname
    print(fname)
    ex.close()
