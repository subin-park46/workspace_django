from django.shortcuts import render, redirect
from .models import MyBoard, MyMember
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    myboard = MyBoard.objects.all().order_by("-id")
    paginator = Paginator(myboard, 10)
    page_num = request.GET.get("page", "1")
    page_obj = paginator.get_page(page_num)

    return render(request, "index.html", {"list": page_obj})


def insert(request):
    if request.method == "GET":
        return render(request, "insert.html")
    elif request.method == "POST":
        myname = request.POST["myname"]
        mytitle = request.POST["mytitle"]
        mycontent = request.POST["mycontent"]

        myboard = MyBoard(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
        myboard.save()

        return redirect("index")

    else:
        return redirect("index")


def detail(request, id):
    return render(request, "detail.html", {"dto": MyBoard.objects.get(id=id)})


def update(request, id):
    if request.method == "GET":
        return render(request, "update.html", {"dto": MyBoard.objects.get(id=id)})
    elif request.method == "POST":
        mytitle = request.POST["mytitle"]
        mycontent = request.POST["mycontent"]

        myboard = MyBoard.objects.filter(id=id)
        update_title = myboard.update(mytitle=mytitle)
        update_content = myboard.update(mycontent=mycontent)
        if update_title + update_content == 2:
            return redirect(f"/detail/{id}")
        else:
            return redirect(f"/update/{id}")
    else:
        return redirect("index")


def delete(request, id):
    delete_board = MyBoard.objects.filter(id=id).delete()
    if delete_board[0]:
        return redirect("index")
    else:
        return redirect(f"/detail/{id}")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        myname = request.POST["myname"]
        mypassword = request.POST["mypassword"]
        myemail = request.POST["myemail"]

        mymember = MyMember(myname=myname, mypassword=make_password(mypassword), myemail=myemail)
        mymember.save()
        return redirect("login")

    else:
        return redirect("index")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        myname = request.POST["myname"]
        mypassword = request.POST["mypassword"]

        mymember = MyMember.objects.get(myname=myname)
        if check_password(mypassword, mymember.mypassword):
            request.session["myname"] = mymember.myname
            return redirect("index")
        else:
            return redirect("login")


def logout(request):
    del request.session["myname"]
    return redirect("index")
