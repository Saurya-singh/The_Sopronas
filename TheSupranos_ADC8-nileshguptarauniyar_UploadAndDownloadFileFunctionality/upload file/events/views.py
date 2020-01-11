from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['doc']
        file_object = FileSystemStorage()
        file_object.save(uploaded_file.name, uploaded_file)
    return render(request,'upload.html')