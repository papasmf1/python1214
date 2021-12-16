# web1.py 
#웹 크롤링을 위한 선언 
from bs4 import BeautifulSoup

#연습용 파일을 로딩(Read Text)
#메서드 체인:메서드를 연속으로 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

#검색이 용이한 객체(HTML태그에서 검색) 
soup = BeautifulSoup(page, "html.parser")

#전체 내용 보기 
#print( soup.prettify() )

#<p> 전부 검색 ==> List에 담아서 리턴 
#print( soup.find_all("p") )

#<p>한개
#print( soup.find("p") )

#검색조건: <p class="outer-text">
#파이썬의 예약어(키워드)는 변수명, 인자이름을 사용하면 안됨
#수많은 <p>에서 필터링(걸러내기) 
#print( soup.find_all("p", class_ = "outer-text") )

#<p id="first"> 검색
#print( soup.find_all("p", id="first") )

#내부에 컨텐츠만 가져오기
result = soup.find_all("p")
print("갯수:{0}".format( len(result) ))

for item in soup.find_all("p"):
    #태그 내부에 문자열만 리턴 
    content = item.text.strip()
    content = content.replace("\n", "")
    print(content)



