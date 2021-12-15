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

print( dir() )

