# Function3.py
result = list(range(1,11))
print(result)
#년도를 생성
years = list(range(2000,2022))
print(years)
#-1 감소
numbers = list(range(10,0,-1))
print(numbers)

#리스트 컴프리헨션(한줄로 반복, 필터링, 가공하기)
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print(result)


#필터링하는 함수

