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
