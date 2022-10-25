from django.shortcuts import render, redirect
from .forms import MyMemberForm

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": MyMemberForm()})
    else:
        form = MyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('register')

def result(request):
    return render(request, 'result.html')