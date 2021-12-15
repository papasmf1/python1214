# DemoTimeDate.py 
#import time 

#print( dir(time) )

# print( time.time() )
# time.sleep(10)
# print( time.time() )

# print("---표준시간 우리시간---")
# print( time.gmtime() )
# print( time.localtime() )

#날짜와 시간
from datetime import * 

#print( dir() )

d1 = date(2021, 12, 25)
print( d1 )

d2 = date.today() 
print( d2 )

#주문받고 100일 
d3 = timedelta(days=100)

print( d2 + d3 )

#파일이름 
print("c:\\work\\test.txt")
print("c:\\work\\newfile.txt")
#소문자 r을 붙이는 방법
print(r"c:\work\test.txt")
print(r"c:\work\newfile.txt")

from os.path import * 

#print( dir() )

print( abspath("python.exe") )
print( basename("c:\\python38\\python.exe") )
print( getsize("c:\\python38\\python.exe") )
print( exists("c:\\python38\\python.exe") )

#운영체제 관련 정보 
from os import * 

print("운영체제이름:", name )
#system("notepad.exe")

#임의의 정수, 실수 생성
import random

print( random.random() )
print( random.random() )

#임의의 정수를 생성 
print( [random.sample(range(20), 10)] )
print( [random.sample(range(20), 10)] )
print( [random.sample(range(20), 10)] )

#로또 번호 생성기
lotto = list(range(1,46))
print( lotto )
random.shuffle(lotto)
print( lotto )

#파일 리스트 
import glob 
result = glob.glob("c:\\work\\*.py")
#print(result)
for item in result:
    print( basename(item) )


