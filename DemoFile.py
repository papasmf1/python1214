# DemoFile.py

#문자열 결합 연산
url = "http://www.credu.com/?page=" + str(1)  
print(url)

#위치 지정
for i in range(1,6):
    print(i,"*",i,"=",i*i)

print("---정렬지정---")
for i in range(1,6):
    print(i,"*",i,"=", str(i*i).rjust(3) )

print("---0으로 채우기---")
for i in range(1,6):
    print(i,"*",i,"=", str(i*i).zfill(3) )

#서식문자
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))

#파일을 쓰기(write text) 인코딩(유니코드)
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
#파이썬이 오래된 언어 
f.write("첫번째\n두번째\n세번째\n")
#버퍼를 비우고 작업 종료
f.close()

