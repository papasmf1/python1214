# Function1.py

#함수 정의
def times(a,b):
    return a*b 

#호출
print( times(3,4) )

#함수 정의
def setValue(newValue):
    x = newValue
    print(x)

#호출
result = setValue(5)
print( result )

#교집합 리스트를 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수를 리스트로 초기화 
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #x라는 글자가 postlist에도 있고 x가 result에 없으면 
        #첫번째 조건도 참이면서 두번째 조건도 참이면 
        if x in postlist and x not in result:
            #리스트형식에 데이터 입력 
            result.append(x)
    return result 

#호출
#중단점 지정
print( intersect("HAM","SPAM") )

