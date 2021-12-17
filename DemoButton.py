# DemoButton.py
#디자이너를 사용하지 않고 100% 코딩 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        #좌측 상단의 꼭지점(x, y)
        btn1.move(100, 20)
        #위젯.시그널명.connect(슬롯메서드)
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 