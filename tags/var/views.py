from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, "var/index.html")


def variable01(request):
    lst = ['python', 'django']
    return render(request, "var/variable01.html", {'lst': lst})


def variable02(request):
    dct = {'class': 'multi', 'name': '동헌'}
    return render(request, "var/variable02.html", {'dct': dct})


def for_loop(request):
    return render(request, "var/forloop.html", {'number': range(1, 11)})


def if01(request):
    return render(request, "var/if01.html", {"user": {"id": "dongheon"}})


def if02(request):
    return render(request, "var/if02.html", {"role": "admin"})


def href(request):
    return render(request, "var/href.html")


def get_post(request):
    if request.method == 'GET':
        return render(request, 'var/get.html')
    elif request.method == "POST":
        return render(request, "var/post.html")
    else:
        return redirect('index')

