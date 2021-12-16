# DemoForm2.py 
# DemoForm2.py(로직을 구현) + DemoForm2.ui(화면을 디자인)
import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic 
#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup
#----선언부------ 

#화면을 로딩
form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

#윈도우 클래스 정의(부모 클래스:QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가
    def firstClick(self):
        f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
        for i in range(1,6):
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print( url )
            data = urllib.request.urlopen(url)
            #검색이 용이한 객체
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text.strip()
                print(title)
                f.write(title + "\n")
        f.close() 
        self.label.setText("네이버 웹툰 리스트 가져오기 종료")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭했습니다~~")

#진입점을 체크해서 실행:C언어에서 진입점(main함수)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_() 