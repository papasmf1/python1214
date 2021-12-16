# db1.py 
#로컬 데이터베이스 엔진
import sqlite3

#연결 객체 생성: 영구적인 파일에 데이터를 저장
con = sqlite3.connect("c:\\work\\test.db")
#커서에서 실제 SQL구문을 실행(Cursor클래스)
cur = con.cursor()
#테이블 구조(테이블 스키마): SQL은 대소문자 구분 안함 
#ANSI SQL 92, 99 표준안 
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 파라메터 처리(?, ?) ==>입력을 받는다.  
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?,?);", (name,phoneNumber))
#다중의 행 데이터 입력(2차원 행열데이터, 2건의 레코드)
datalist = (("tom","010-111"),("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
print( cur.fetchall() )



