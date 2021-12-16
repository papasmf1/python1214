# DemoForm.py 
# DemoForm.py(로직을 구현) + DemoForm.py(화면을 디자인)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType("c:\\work\\DemoForm.ui")[0]

#윈도우 클래스 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt화면")

#진입점을 체크해서 실행:C언어에서 진입점(main함수)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_() 