# 0.import
import mysql.connector
from mysql.connector import Error


try:

    #1.연결/컨넥션 얻기
    conn = mysql.connector.connect(
        host='localhost',           # 호스트
        user='phonebook',           # 사용자명
        password='phonebook',       # 비밀번호
        database='phonebook_db'     # 데이터베이스명
    )

    #2.커서생성
    cursor = conn.cursor()

    #3.SQL문준비 / 바인딩 / 실행
    #--SQL문
    query = """
        select person_id,
                name,
                hp,
                company
        from person
    """

    #--바인딩(튜플)
    # ?가 없으면 생략

    #--실행
    cursor.execute(query)
    resultset = cursor.fetchall()

    #4.결과처리  리스트 [(튜플), (튜플), (튜플)]  -> 리스트[{딕션어리},{딕션어리},{딕션어리}]
    print(resultset)
    person_list = []
    for row in resultset:
        person_vo = {       # 딕션어리 {키-값}
            "person_id": row[0],      # person_id
            "name": row[1],      # name
            "hp": row[2],      # hp
            "company": row[3]      # company
        }
        person_list.append(person_vo)       # 추가하기  포문안에 있는거임
    print(person_list)
    print(person_list[0]["name"])       # 0번째방 이름 뽑기 (키값으로 값찾기)


except Error as e:
    print(f"데이터베이스 오류: {e}")

finally:
    #5.자원정리
    if conn is not None:
        conn.close()

    if cursor is not None:
        cursor.close() 