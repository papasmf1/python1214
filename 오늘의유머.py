# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식 
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
#우리 사이트는 웹봇금지 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}


#파일에 저장
f = open("c:\\work\\today.txt", "wt", encoding="utf-8")
for n in range(1,11):
        #오늘의 유머
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #혹시 한글이 깨지는 경우? 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        #<td class=subject>
        # <a href="/board/view.php?table=bestofbest&amp;no=448797&amp;s_no=448797&amp;page=1" 
        # target="_top">과거 등교거부 사유</a>

        #attrs: 어트리뷰트들 
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        item2 = item.find("a").text.strip()  
                        #print(item2)
                        if (re.search('한국', item2)):
                                print(item2)
                                f.write(item2 + "\n")

                except:
                        pass
        

f.close() 

