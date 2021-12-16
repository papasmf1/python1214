# web2.py 
#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#동적으로 페이지 번호 생성
#수열을 생성하는 함수: range(1,6)
#파일에 저장(Write Text) 
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





                        
