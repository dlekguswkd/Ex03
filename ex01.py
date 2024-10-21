#0.import
import mysql.connector
from mysql.connector import Error


try:
    #1.연결/컨넥션 얻기  (메소드)   순서 바껴도되지만 보통 이순서 
    conn = mysql.connector.connect(
        host="localhost",
        user="phonebook",
        password="phonebook",
        database="phonebook_db"
    )
    print("연결 성공")


    #2.커서생성
    cursor = conn.cursor()

    #3.SQL문준비 / 바인딩 / 실행
    #--SQL문
    query = '''
        insert into person
        values(null, %s, %s, %s)
    '''

    #--바인딩(튜플)
    data = ("유재석", "010-1111-1111", "02-1111-1111")

    #--실행
    cursor.execute(query, data)     # 임시반영 (성공하면 커밋  임시 -> 반영)
    conn.commit()                   # 최종반영

    #4.결과처리
    print(f"{cursor.rowcount} 건 등록되었습니다")          # 결과갯수 알려줌

except Error as e:
    print(f"데이터베이스 오류: {e}")

finally:
    #5.자원정리
    if conn is not None:
        conn.close()

    if cursor is not None:
        cursor.close()                  # 두개를 다 닫아줘야함  



