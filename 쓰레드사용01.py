import sys 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 

#하나의 프로세스 안에서 작업 
#메인쓰레드(UI를 생성하고 작업)
#백그라운드 작업(서버와 통신, 큰 파일 읽기, 연산을 수행):백그라운드 쓰레드 
#CPU(코어 4개 ~ 8개)
#GIL: 한번에 하나의 쓰레드 
class Worker(QThread):
    def run(self):
        while True:
            print("hello~~")
            self.sleep(1)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.start() 

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_() 

        