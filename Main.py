import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QScrollArea):
    def __init__(self):
        super(Window, self).__init__()
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)
        for index in range(100):
            layout.addWidget(QLabel('-------------------------------' + 'Label %02d' % index + '-------------------------------'))
        self.setWidget(widget)
        self.setWidgetResizable(True)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wind = Window()
    sys.exit(app.exec_())