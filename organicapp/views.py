from django.shortcuts import render,redirect
from organicapp import models
from urllib import parse

# Create your views here.
#메인 페이지(홈페이지)
def main(request):
    return render(request,'main/main.html')
#종자리스트
def seed_list(request):
    try:
        page=request.GET['page']
        curpage=int(page)
    except Exception as e:
        curpage=1
    seed_data=models.seed_list(curpage)
    totalpage = models.seed_totalpage()
    count=models.seed_count()
    sd=[]
    #SELECT no,cno,name,img,price
    for row in seed_data:
        data={"no":row[0],"cno":row[1],"name":row[2],"image":row[3],"price":row[4]}
        sd.append(data)
    print(sd)

    block=10
    startPage=((curpage-1)//block*block)+1
    endPage=((curpage-1)//block*block)+block
    if endPage > totalpage:
        endPage=totalpage
    data={"curpage":curpage,"totalPage":totalpage,"startPage":startPage,"endPage":endPage,"sd":sd,"range":range(startPage,endPage+1),"count":count}
    return render(request,'seed/seed_list.html',data)

#종자 디테일
def seed_detail(request):
    no=request.GET['no']
    detail_data=models.seed_detail(int(no))
    for f in detail_data:
        print(f)
    #카테고리별 이름 구분
    cons=''
    if detail_data[1]==1:
        cons="꽃씨"
    elif detail_data[1]==2:
        cons="과일과 채소"
    elif detail_data[1]==3:
        cons="곡물과 식량작물"
    elif detail_data[1]==4:
        cons="특`약용작물"
    elif detail_data[1]==5:
        cons="허브 등 기타"
    # no,cno,name,pay,delivery,
    # delivery_pay,detail_image,main_image
    sd={
        "no":detail_data[0],
        "cno":cons,
        "name":detail_data[2],
        "pay":detail_data[3],
        "delivery":detail_data[4],
        "delivery_pay":detail_data[5],
        "detail_image":detail_data[6],
        "main_image":detail_data[7]
    }
    return render(request,'seed/seed_detail.html',sd)
#재배기술(해충)게시판
def plantation_insect(request):
    try:
        page=request.GET['page']
        curpage=int(page)
    except Exception as e:
        curpage=1
    plantation_in_allData=models.plantation_iList(curpage)
    totalpage=models.plantation_iPage()
    db = []
    for i in plantation_in_allData:
        print(i)
        #no,cno,title,name,regdate,hit
        idata={
            "no":i[0],
            "cno":i[1],
            "title":i[2],
            "name":i[3],
            "regdate":i[4],
            "hit":i[5]
        }
        db.append(idata)
    block = 10
    startPage = ((curpage - 1) // block * block) + 1
    endPage = ((curpage - 1) // block * block) + block
    if endPage > totalpage:
        endPage = totalpage
    return render(request,'plantation/plantation_list.html',{"curpage":curpage,"totalpage":totalpage,"list":db,"range":range(startPage,endPage+1)})
#해충 디테일
def plantation_idetail(request):
    #no, cno, title, name, regdate, hit, content, main_img
    no=request.GET['no']
    di=models.plantation_iDetail(int(no))
    cons = ''
    if di[1] == 1:
        cons = "재배기술"
    elif di[1] == 2:
        cons = "병해충진단/방제"
    dd={
        "no":di[0],
        "cno":cons,
        "title":di[2],
        "name":di[3],
        "regdate":di[4],
        "hit":di[5],
        "content":di[6],
        "main_img":di[7]
    }
    return render(request,'plantation/plantation_idetail.html',dd)

#이미지 게시판 리스트
def plantation_imageList(request):
    try:
        page=request.GET['page']
        curpage=int(page)
    except Exception as e:
        curpage=1
    image_data=models.plantation_imageList(curpage)
    totalpage = models.plantation_imagePage()
    md=[]
    #no,cno,title,name,regdate,hit,main_img
    for row in image_data:
        data={"no":row[0],"cno":row[1],"title":row[2],"name":row[3],"regdate":row[4],"hit":row[5],"main_img":row[6]}
        md.append(data)
    print(md)
    block=10
    startPage=((curpage-1)//block*block)+1
    endPage=((curpage-1)//block*block)+block
    if endPage > totalpage:
        endPage=totalpage
    data={"curpage":curpage,"totalPage":totalpage,"startPage":startPage,"endPage":endPage,"md":md,"range":range(startPage,endPage+1)}
    return render(request,'plantation/image_list.html',data)
#이미지 게시판 상세보기
def plantation_imageDetail(request):
    #no,cno,title,name,regdate,hit,main_img
    no = request.GET['no']
    di = models.plantation_imageDetail(int(no))
    cons = ''
    if di[1] == 1:
        cons = "재배기술"
    md = {
        "no": di[0],
        "cno": cons,
        "title": di[2],
        "name": di[3],
        "regdate": di[4],
        "hit": di[5],
        "main_img": di[6]
    }
    return render(request,'plantation/image_detail.html', md)
#매거진 리스트
def plantation_magazineList(request):
    try:
        page = request.GET['page']
        curpage = int(page)
    except Exception as e:
        curpage = 1
    magazine_data = models.plantation_magazineList(curpage)
    totalpage = models.plantation_magazinePage()
    mad = []
    # no,cno,title,name,regdate,hit,main_img
    for row in magazine_data:
        data = {"no": row[0], "cno": row[1], "title": row[2], "name": row[3], "regdate": row[4], "hit": row[5],
                "main_img": row[6]}
        mad.append(data)
    print(mad)
    block = 10
    startPage = ((curpage - 1) // block * block) + 1
    endPage = ((curpage - 1) // block * block) + block
    if endPage > totalpage:
        endPage = totalpage
    data = {"curpage": curpage, "totalPage": totalpage, "startPage": startPage, "endPage": endPage, "mad": mad,
            "range": range(startPage, endPage + 1)}
    return render(request, 'plantation/magazine_list.html', data)
#매거진 디테일
def plantation_magazineDetail(request):
    # no,cno,title,name,regdate,hit,main_img
    no = request.GET['no']
    di = models.plantation_magazineDetail(int(no))
    cons = ''
    if di[1] == 1:
        cons = "재배기술"
    posters = di[6].split(",")
    print(posters)
    md = {
        "no": di[0],
        "cno": cons,
        "title": di[2],
        "name": di[3],
        "regdate": di[4],
        "hit": di[5],
        "main_img": posters
    }
    return render(request, 'plantation/magazine_detail.html', md)

#답변형 게시판 관련
def board_list(request):
    try:
          page=request.GET['page']
          curpage=int(page)
    except Exception as e:
          curpage=1
    board_all_data=models.board_list(curpage)
    totalpage=models.board_totalpage()
    bd=[]
    for row in board_all_data:
        r=range(1,row[5]+1)
        print(r,row[5])
        data={"no":row[0],"subject":row[1],"name":row[2],"regdate":row[3],"hit":row[4],"range":r,"group_tab":row[5]}
        bd.append(data)
    return render(request,'board/list.html',{"curpage":curpage,"totalpage":totalpage,"list":bd})

def board_insert(request):
    return render(request,'board/insert.html')
def board_insert_ok(request):
    name=request.POST['name']
    subject=request.POST['subject']
    content=request.POST['content']
    pwd=request.POST['pwd']
    data=(name,subject,content,pwd)
    models.board_insert(data)
    return redirect('/board/list/')
def board_detail(request):
    #no,name,subject,content,TO_CHAR(regdate,'YYYY-MM-DD'),hit
    no=request.GET['no']
    detail_data=models.board_detail(int(no))
    dd={"no":detail_data[0],"name":detail_data[1],"subject":detail_data[2],"content":detail_data[3],"regdate":detail_data[4],"hit":detail_data[5]}
    return render(request,'board/detail.html',dd) #forward {"dd",dd}  dd

#수정 , 삭제 , 답변
def board_update_data(request):
    no=request.GET['no']
    u_data=models.board_updata_data(no)
    #no,name,subject,content
    ud={"no":u_data[0],"name":u_data[1],"subject":u_data[2],"content":u_data[3]}
    return render(request,'board/update.html',ud)
def board_update_ok(request):
    name=request.POST['name']
    subject=request.POST['subject']
    content=request.POST['content']
    pwd=request.POST['pwd']
    no=request.POST['no']
    udata=(no,name,subject,content,pwd)
    result=models.board_update_ok(udata)
    print(f"result={result}")
    return render(request,'board/update_ok.html',{"result":result,"no":no})

#답변
def board_reply(request):
    no=request.GET['no']
    return render(request,'board/reply.html',{"no":no})

def board_reply_ok(request):
    pno=request.POST['pno']
    name = request.POST['name']
    subject = request.POST['subject']
    content = request.POST['content']
    pwd = request.POST['pwd']
    rdata=(pno,name,subject,content,pwd)
    models.board_reply(rdata)
    return redirect("/board/list/")

def board_delete(request):
     no=request.GET['no']
     return render(request,'board/delete.html',{"no":no})

def board_delete_ok(request):
     no=request.POST['no']
     pwd=request.POST['pwd']
     result=models.board_delete(int(no),pwd)
     return render(request,'board/delete_ok.html',{"result":result})

def introduce_hong(request):
    return render(request,'introduce/hong.html')

def login(request):
    id=request.POST['id']
    print(id)
    pwd=request.POST['pwd']
    print(pwd)
    result=models.login(id,pwd)
    print(result)
    if not (result=='NOID' and result=='NOPWD'):
        request.session['id']=id
        request.session['name']=result
    return render(request,'main/login.html',{"result":result})
def logout(request):
    request.session.clear()
    return redirect('/organic/main/')
def login_main(request):
    return render(request,'main/login_main.html')
#원예도서
def book_list(request):
    try:
        page=request.GET['page']
        curpage=int(page)
    except Exception as e:
        curpage=1
    book_data=models.book_list(curpage)
    totalpage=models.book_totalPage()
    bd=[]
    for i in book_data:
        data = {"no":i[0],"title":i[1],"book_img":i[2]}
        bd.append(data)

    block=5
    startPage=((curpage-1)//block*block)+1
    endPage=((curpage-1)//block*block)+block
    if endPage > totalpage:
        endPage=totalpage
    data={"curpage":curpage,"totalpage":totalpage,"startPage":startPage,"endPage":endPage,"range":range(startPage,endPage+1),"bd":bd}
    return render(request,'book/book_list.html',data)
def book_detail(request):
    no=request.GET['no']
    detail_data=models.book_detail(no)
    bd={
        "no":detail_data[0],
        "cno":detail_data[1],
        "title":detail_data[2],
        "name":detail_data[3],
        "regdate":detail_data[4],
        "hit":detail_data[5],
        "book_img":detail_data[6],
        "content":detail_data[7]
    }
    return render(request,"book/book_detail.html",bd)

