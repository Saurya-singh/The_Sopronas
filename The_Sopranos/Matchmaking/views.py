from django.shortcuts import render,redirect
from .forms import statusform
from .models import Status

# Create your views here.

def home(request):
    return render(request, 'home.html')
def notification(request):
    return render(request, 'notification.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def search(request):
    return render(request, 'search.html')

def status_list(request):
    context = {'status_list': Status.objects.all()}
    return render(request, "./status_list.html", context)


             
def status_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = statusform()
        else:
            status = Status.objects.get(pk=id)
            form = statusform(instance=status)
        return render(request, "./status_form.html", {'form': form})
    else:
        if id == 0:
            form = statusform(request.POST)
        else:
            status = Status.objects.get(pk=id)
            form = statusform(request.POST,instance= status)
        if form.is_valid():
            form.save()
        return redirect('/list')

def status_delete(request,id):
    status = Status.objects.get(pk=id)
    status.delete()
    return redirect('/list')
    