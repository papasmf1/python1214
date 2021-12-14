# -*- 생성자와 소멸자 -*-
class MyClass:
    #생성자 메서드(초기화 담당)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #소멸자 메서드(가장 마지막에 실행)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스를 생성
d = MyClass(5)
#메모리 관리는 자동~~ 
#del d 

print("전체 코드 실행 종료")

#가비지 컬렉션은 주기적으로 실행 