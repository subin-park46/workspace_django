from django.shortcuts import render, redirect
from .models import MyBoard, MyMember
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    # return render(request, "index.html", {"list": MyBoard.objects.all().order_by('-id')}) # id 기준으로 정렬, -는 DESC
    myboard = MyBoard.objects.all().order_by("-id")
    paginator = Paginator(myboard, 10) # 전체 데이터에서 10개씩 자름
    page_num = request.GET.get('page', '1') # GET 방식으로 가져오고 있으면 PAGE, 없으면 1

    page_obj = paginator.get_page(page_num)

    """
    print("*" * 10)
    print(type(page_obj))
    print(page_obj.count) # 총 모델 갯수
    print(page_obj.paginator.num_pages) # 총 page 갯수
    print(page_obj.paginator.page_range) # 총 page에 대한 range 객체
    print(page_obj.has_next()) # 다음 페이지 유무를 boolean
    print(page_obj.has_previous()) # 이전 페이지 유무를 boolean
    try:
        print(page_obj.next_page_number()) # 다음 페이지 번호
        print(page_obj.previous_page_number()) # 이전 페이지 번호
    except:
        pass
    print(page_obj.start_index()) # 해당 페이지에서 첫번째 모델에 대한 인덱스
    print(page_obj.end_index()) # 해당 페이지에서 마지막 모델에 대한 인덱스
    """

    return render(request, "index.html", {"list": page_obj})
def insert(request):
    if request.method == "GET":
        return render(request, "insert.html")
    elif request.method == "POST":
        myname = request.POST["myname"]
        mytitle = request.POST["mytitle"]
        mycontent = request.POST["mycontent"]

        result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now()) # 데이터 저장
        if result: # 제대로 값이 저장됐으면
            return redirect("index")
        else: # 제대로 안됐으면
            return redirect("insert")
    else:
        return redirect("/")


def detail(request, id):
    return render(request, "detail.html", {"dto": MyBoard.objects.get(id=id)}) # get : 조건 맞는 하나 가져옴.

def update(request, id):
    if request.method == "GET":
        return render(request, "update.html", {"dto": MyBoard.objects.get(id=id)})
    elif request.method == "POST":
        mytitle = request.POST["mytitle"]
        mycontent = request.POST["mycontent"]

        myboard = MyBoard.objects.filter(id=id)
        result_title = myboard.update(mytitle=mytitle)
        result_content = myboard.update(mycontent=mycontent)

        if result_title + result_content == 2:
            return redirect(f"/detail/{id}")
        else:
            return redirect(f"/update/{id}")
    else:
        return redirect("/")

def delete(request, id):
    result_delete = MyBoard.objects.filter(id=id).delete()

    if result_delete[0]: # 0번지에 값이 제대로 들어있다면
        return redirect("index")
    else:
        return redirect(f"/detail/{id}")

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        myname = request.POST["myname"]
        mypassword = request.POST["mypassword"]
        myemail = request.POST["myemail"]

        mymember = MyMember(myname=myname, mypassword=make_password(mypassword), myemail=myemail)
        mymember.save()

        return redirect("/")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        myname = request.POST["myname"]
        mypassword = request.POST["mypassword"]

        mymember = MyMember.objects.get(myname=myname)

        if check_password(mypassword, mymember.mypassword): # 두개가 같다면
            request.session['myname'] = mymember.myname
            return redirect('index')
        else:
            return redirect("login")

def logout(request):
    del request.session["myname"]
    return redirect("/")