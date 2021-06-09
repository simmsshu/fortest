from PyQt5.QtWidgets import QMainWindow,QPushButton,QLabel,QTableWidget,QLineEdit,QWidget,QApplication
from PyQt5.QtGui import QIcon

class AppserverWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.appServerWindow()
    def appServerWindow(self):
        self.setWindowIcon(QIcon("kibana.png"))
        self.setWindowTitle("APPserverl日志")
        # lab1=QLabel("AccountID")
        # box1=QLineEdit()
        self.setGeometry(40,40,1000,900)

        self.show()
