# DemoStr.py 

#str클래스의 멤버 목록 
#print( dir(str) )

#선택한 라인을 주석: ctrl + / 
# 웹에서 또는 텍스트파일을 로딩한 경우 
# strA = "<<<  python is very powerful  >>>"
# result = strA.strip("<> ")
# print( result )
# result2 = result.replace("python", "python egg")
# print( result2 )
# print( "demo.ppt".endswith("ppt") )
# print("알파벳과 숫자로 구성")
# print( "MBC2580".isalnum() )
# print( "MBC:2580".isalnum() )
# print( "2580".isdecimal() )
# print( result2.count("p") )
# print( result2.count("p", 7) )
# print("---리스트로 받기---")
# lst = result2.split()
# print( lst )
# print("---하나의 문자열---")
# print( ":)".join(lst) )

# #반복되는 문자열 생성(VBA) ==> 오피스(VBA -> Python)
# names = ["전우치","이순신","김길동"]
# for name in names:
#     print("안녕하세요 {0}님 추운 겨울입니다.".format(name))
#     print("=" * 40)


#정규 표현식:특정한 패턴 검색
import re 

result = re.match("[0-9]*th", "35th")
result2 = re.search("[0-9]*th", "35th")
print( result.group() )
print( result2.group() )

#ctrl + F5 
#정확하게 일치
result = re.match("[0-9]*th", "  35th")
#처음부터 끝까지 검색 
result2 = re.search("[0-9]*th", "  35th")
print( result )
print( result2.group() )

result = re.search("apple", "this is apple")
print( result.group() )

#년도 
result = re.search("\d{4}", "올해는 2021년입니다.")
print( result.group() )

print("---우편번호---")
result = re.search("\d{5}", "우리 동네는 52300입니다.")
print( result.group() )




