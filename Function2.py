# Function2.py 

#불변형식과 가변형식
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(lst)
print( id(lst) )

#LGB 이름 해석 규칙
#전역변수 
x = 2
#함수 정의
def func1(a):
    return a+x 

#호출
print( func1(1) )

def func2(a):
    #지역변수 
    x = 5 
    return a+x 

#호출
print( func2(1) )

#기본값이 있는 경우
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자(매개변수명을 지정)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

#가변인자(입력되는 인자의 갯수가 다양한 경우)
#유니크한 글자를 리턴 
#*는 내부에서 Tuple로 처리
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print( union("HAM","SPAM") )
print( union("HAM","SPAM","EGG") )

#정의되지 않은 인자 처리 
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출 
print( userURIBuilder("credu.com","80",id="kim",name="mike") )
print( userURIBuilder("credu.com","80",id="kim",name="mike",   
    age="30") )

#람다함수(이름이 없는 간결한 함수 정의)
g = lambda x,y:x*y
print( g(3,4) )
print( g(5,6) )
