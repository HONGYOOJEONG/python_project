from django.db import models
import cx_Oracle
# Create your models here.
def getConnection():
    try:
        conn=cx_Oracle.connect("hr/happy@localhost:1521/xe")
    except Exception as e:
        print(e)
    return conn
#종자리스트
def seed_list(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=9
    start=(rowSize*page)-(rowSize-1)
    end=rowSize*page
    sql=f"""
            SELECT no,cno,name,image,price,num
            FROM (SELECT no,cno,name,image,price,rownum as num
            FROM (SELECT /*+ INDEX_ASC(seed_main sm_no_pk) */ no,cno,name,image,price
            FROM seed_main))
            WHERE num BETWEEN {start} AND {end}
        """
    cursor.execute(sql)
    seed_data=cursor.fetchall()
    print(seed_data)
    cursor.close()
    conn.close()
    return seed_data
def seed_totalpage():
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"SELECT CEIL(COUNT(*)/9.0) FROM seed_main"
    cursor.execute(sql)
    total=cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]
#종자 갯수
def seed_count():
    conn=getConnection()
    cursor=conn.cursor()
    sql="SELECT COUNT(*) FROM seed_main"
    cursor.execute(sql)
    count=cursor.fetchone()
    cursor.close()
    conn.close()
    return count[0]

#종자 디테일
def seed_detail(no):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,cno,name,pay,delivery,delivery_pay,detail_image,main_image
            FROM seed_detail
            WHERE no={no}
        """
    cursor.execute(sql)
    data=cursor.fetchone()
    seed_detail_data=(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
    cursor.close()
    conn.close()
    return seed_detail_data
#재배기술(벌레)_게시판
def plantation_iList(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=10
    start=(rowSize*page)-(rowSize-1)
    end=rowSize*page
    sql=f"""
            SELECT no,cno,title,name,regdate,hit,num
            FROM (SELECT no,cno,title,name,regdate,hit,rownum as num
            FROM (SELECT no,cno,title,name,regdate,hit
            FROM plantation_insect ORDER BY no ASC))
            WHERE num BETWEEN {start} AND {end}
        """
    cursor.execute(sql)
    insect_data=cursor.fetchall()
    cursor.close()
    conn.close()
    return insect_data
#재배기술(벌레)_게시판 총페이지
def plantation_iPage():
    conn=getConnection()
    cursor=conn.cursor()
    sql="SELECT CEIL(COUNT(*)/10.0) FROM plantation_insect"
    cursor.execute(sql)
    iList_totalpage=cursor.fetchone()
    cursor.close()
    conn.close()
    return iList_totalpage[0]
#해충게시판 디테일
def plantation_iDetail(no):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,cno,title,name,regdate,hit,content,main_img
            FROM plantation_insect
            WHERE no={no} 
            
        """
    cursor.execute(sql)
    dd=cursor.fetchone()
    detail_idata=(dd[0],dd[1],dd[2],dd[3],dd[4],dd[5],dd[6].read(),dd[7])
    cursor.close()
    conn.close()
    return detail_idata


# 재배기술 이미지 게시판
def plantation_imageList(page):
    conn = getConnection()
    cursor = conn.cursor()
    rowSize = 9
    start = (rowSize * page) - (rowSize - 1)
    end = rowSize * page
    sql = f"""
            SELECT no,cno,title,name,regdate,hit,main_img,num
            FROM (SELECT no,cno,title,name,regdate,hit,main_img,rownum as num
            FROM (SELECT /*+ INDEX_ASC(plantation_imgboard pi_no_pk) */ no,cno,title,name,regdate,hit,main_img
            FROM plantation_imgboard ORDER BY no DESC))
            WHERE num BETWEEN {start} AND {end}
        """
    cursor.execute(sql)
    board_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return board_data


# 이미지_게시판 총페이지
def plantation_imagePage():
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT CEIL(COUNT(*)/10.0) FROM plantation_imgboard"
    cursor.execute(sql)
    iList_totalpage = cursor.fetchone()
    cursor.close()
    conn.close()
    return iList_totalpage[0]

#이미지 디테일
def plantation_imageDetail(no):
    conn = getConnection()
    cursor = conn.cursor()
    sql = f"""
            SELECT no,cno,title,name,regdate,hit,main_img
            FROM plantation_imgboard
            WHERE no={no} 

        """
    cursor.execute(sql)
    dd = cursor.fetchone()
    detail_idata = (dd[0], dd[1], dd[2], dd[3], dd[4], dd[5],dd[6])
    cursor.close()
    conn.close()
    return detail_idata

# 매거진 게시판 리스트
def plantation_magazineList(page):
    conn = getConnection()
    cursor = conn.cursor()
    rowSize = 10
    start = (rowSize * page) - (rowSize - 1)
    end = rowSize * page
    sql = f"""
            SELECT no,cno,title,name,regdate,hit,main_img,num
            FROM (SELECT no,cno,title,name,regdate,hit,main_img,rownum as num
            FROM (SELECT /*+ INDEX_ASC(plantation_magazine pm_no_pk) */ no,cno,title,name,regdate,hit,main_img
            FROM plantation_magazine ORDER BY no DESC))
            WHERE num BETWEEN {start} AND {end}
        """
    cursor.execute(sql)
    magazine_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return magazine_data


# 매거진 게시판 총페이지
def plantation_magazinePage():
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT CEIL(COUNT(*)/10.0) FROM plantation_magazine"
    cursor.execute(sql)
    mList_totalpage = cursor.fetchone()
    cursor.close()
    conn.close()
    return mList_totalpage[0]

#매거진 디테일
def plantation_magazineDetail(no):
    conn = getConnection()
    cursor = conn.cursor()
    sql = f"""
            SELECT no,cno,title,name,regdate,hit,main_img
            FROM plantation_magazine
            WHERE no={no} 
        """
    cursor.execute(sql)
    dd = cursor.fetchone()
    detail_mdata = (dd[0], dd[1], dd[2], dd[3], dd[4], dd[5],dd[6])
    cursor.close()
    conn.close()
    return detail_mdata

#답변형게시판
def board_list(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=10
    start=(rowSize*page)-(rowSize-1)
    end=rowSize*page
    sql=f"""
           SELECT no,subject,name,TO_CHAR(regdate,'YYYY-MM-DD'),hit,group_tab,num
           FROM (SELECT no,subject,name,regdate,hit,group_tab,rownum as num
           FROM (SELECT no,subject,name,regdate,hit,group_tab
           FROM django_board ORDER BY group_id DESC , group_step ASC))
           WHERE num BETWEEN {start} AND {end}
          """
    cursor.execute(sql)
    board_data=cursor.fetchall()
    cursor.close()
    conn.close()
    return board_data

#총페이지 읽기
def board_totalpage():
    conn=getConnection()
    cursor=conn.cursor()
    sql="SELECT CEIL(COUNT(*)/10.0) FROM django_board"
    cursor.execute(sql)
    total=cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]

#데이터 추가
def board_insert(board_vo):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            INSERT INTO django_board(no,name,subject,content,pwd,group_id) 
            VALUES(py_no_seq.nextval,:1,:2,:3,:4,(SELECT NVL(MAX(group_id)+1,1) FROM django_board))
          """
    cursor.execute(sql,board_vo)
    conn.commit()
    cursor.close()
    conn.close()

#상세보기
def board_detail(no):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
             UPDATE django_board SET
             hit=hit+1
             WHERE no={no}
          """
    cursor.execute(sql)
    conn.commit()
    cursor.close()

    cursor=conn.cursor()
    sql=f"""
            SELECT no,name,subject,content,TO_CHAR(regdate,'YYYY-MM-DD'),hit
            FROM django_board
            WHERE no={no}
          """
    cursor.execute(sql)
    dd=cursor.fetchone()
    detail_data=(dd[0],dd[1],dd[2],dd[3].read(),dd[4],dd[5])
    cursor.close()
    conn.close()
    return detail_data

def board_updata_data(no):
    conn = getConnection()
    cursor = conn.cursor()
    sql = f"""
                SELECT no,name,subject,content
                FROM django_board
                WHERE no={no}
           """
    cursor.execute(sql)
    dd = cursor.fetchone()
    update_data = (dd[0], dd[1], dd[2], dd[3].read())
    cursor.close()
    conn.close()
    return update_data

def board_update_ok(udata):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT pwd FROM django_board
            WHERE no={udata[0]}
          """
    print(sql)
    cursor.execute(sql)
    db_pwd=cursor.fetchone()
    cursor.close()
    result=False
    if db_pwd[0]==udata[4]:
        result=True
        #실제 데이터 추가
        cursor=conn.cursor()
        sql=f"""
                UPDATE django_board SET
                name='{udata[1]}',subject='{udata[2]}',content='{udata[3]}'
                WHERE no={udata[0]}
              """
        print(sql)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    else:
        result=False
    conn.close()
    print(f"model:{result}")
    return result

def board_reply(rdata):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT group_id , group_step,group_tab 
            FROM django_board
            WHERE no={rdata[0]}
          """
    cursor.execute(sql)
    pvo=cursor.fetchone()
    cursor.close()
    # 답변 구현 =조절
    cursor=conn.cursor()
    sql=f"""
            UPDATE django_board SET
            group_step=group_step+1
            WHERE group_id={pvo[0]} and group_step>{pvo[1]}
          """
    cursor.execute(sql)
    conn.commit()
    cursor.close()

    # 실제 데이터 추가
    cursor=conn.cursor()
    sql=f"""
           INSERT INTO django_board(no,name,subject,content,pwd,group_id,group_step,group_tab,root)
           VALUES(py_no_seq.nextval,:1,:2,:3,:4,:5,:6,:7,:8)
          """
    data=(rdata[1],rdata[2],rdata[3],rdata[4],pvo[0],pvo[1]+1,pvo[2]+1,rdata[0])
    cursor.execute(sql,data)
    conn.commit()
    cursor.close()

    cursor=conn.cursor()
    sql=f"""
            UPDATE django_board SET
            depth=depth+1
            WHERE no={rdata[0]}
          """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

#삭제
def board_delete(no,pwd):
    conn=getConnection()
    cursor=conn.cursor()
    #비밀번호 검색
    sql=f"""
            SELECT pwd,root,depth 
            FROM django_board
            WHERE no={no}
          """
    cursor.execute(sql)
    info=cursor.fetchone()
    cursor.close()
    #삭제

    result=False
    if pwd==info[0] :
        result=True
        if info[2]==0: #답변이 없는 경우
            cursor = conn.cursor()
            sql=f"""
                    DELETE FROM django_board
                    WHERE no={no}
                  """
            cursor.execute(sql)
            conn.commit()
            cursor.close()
        else: #답변이 있는 경우
            cursor=conn.cursor()
            sql=f"""
                    UPDATE django_board SET
                    subject='관리자가 삭제한 게시물입니다',
                    content='관리자가 삭제한 게시물입니다'
                    WHERE no={no}
                  """
            cursor.execute(sql)
            conn.commit()
            cursor.close()

        cursor=conn.cursor()
        sql=f"""
               UPDATE django_board SET
               depth=depth-1
               WHERE no={info[1]}
             """
        cursor.execute(sql)
        conn.commit()
        cursor.close()
    else:
        result=False
    conn.close()
    return result

def introduce_hong():
    pass

def login(id,pwd):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT COUNT(*) FROM member
            WHERE id='{id}'
        """
    cursor.execute(sql)
    count=cursor.fetchone()
    print(count)
    cursor.close()
    result=''
    if count[0]==0:
        result='NOID'
        print(result)
    else:
        cursor=conn.cursor()
        sql=f"""
                SELECT pwd,name FROM member
                WHERE id='{id}'
            """
        cursor.execute(sql)
        db_data=cursor.fetchone()
        print(db_data)
        cursor.close()
        db_pwd=db_data[0]
        name=db_data[1]
        if db_pwd!=pwd:
            result='NOPWD'
            print(result)
    conn.close()
    return result
def login_main():
    pass
#원예 도서 리스트
def book_list(page):
    conn=getConnection()
    cursor=conn.cursor()
    rowSize=9
    start=(rowSize*page)-(rowSize-1)
    end=(rowSize*page)
    sql=f"""
            SELECT no,title,book_img,num
            FROM (SELECT no,title,book_img,rownum as num
            FROM (SELECT /*+ INDEX_ASC(plantation_book pb_no_pk) */ no,title,book_img
            FROM plantation_book))
            WHERE num BETWEEN {start} AND {end} 
        """
    cursor.execute(sql)
    book_data=cursor.fetchall()
    cursor.close()
    conn.close()
    return book_data
def book_totalPage():
    conn=getConnection()
    cursor=conn.cursor()
    sql="SELECT CEIL(COUNT(*)/9.0) FROM plantation_book"
    cursor.execute(sql)
    total=cursor.fetchone()
    cursor.close()
    conn.close()
    return total[0]
#원예도서 상세보기
def book_detail(no):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT no,cno,title,name,regdate,hit,book_img,content
            FROM plantation_book
            WHERE no={no}
        """
    cursor.execute(sql)
    bd=cursor.fetchone()
    book_dData=(bd[0],bd[1],bd[2],bd[3],bd[4],bd[5],bd[6],bd[7])
    cursor.close()
    conn.close()
    return book_dData
def join_ok():
    conn = getConnection()
    cursor = conn.cursor()
    sql=f"""
            INSERT INTO member(id,pwd,name,email,add1,add2,phone1,admin)
           VALUES(:1,:2,:3,:4,:5,:6,:7,:8,'n')
        """
def idCheck(id):
    conn=getConnection()
    cursor=conn.cursor()
    sql=f"""
            SELECT id FROM member
            WHERE id='{id}'
        """
    cursor.execute(sql)
    id_check=cursor.fetchone()
    cursor.close()
    conn.close()
    return id_check[0]