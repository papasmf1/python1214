# db1.py 
#로컬 데이터베이스 엔진
import sqlite3

#연결 객체 생성: 임시로 메모리 저장(Connection) 
con = sqlite3.connect(":memory:")

#커서에서 실제 SQL구문을 실행(Cursor클래스)
cur = con.cursor()

#테이블 구조(테이블 스키마): SQL은 대소문자 구분 안함 
#ANSI SQL 92, 99 표준안 
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    #print( row[0] + " , " + row[1] )
    print(row)




