from django.shortcuts import render

# Create your views here.
def intex(request):
    return render(request, "var/index.html")

def variable01(request):
    lst = ['python', 'django']
    return render(request, "var/variable01.html", {'lst': lst})