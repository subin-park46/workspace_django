from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def upload_process(request):
    upload_file = request.FILES['uploadfile']
    uploaded = default_storage.save(upload_file.name, ContentFile(upload_file.read()))

    return render(request, 'download.html', {'filename': uploaded})

def download_process(request, filename):
    response = HttpResponse(default_storage.open(filename).read(), content_type='application/force-download')

    return response
