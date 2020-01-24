from django.shortcuts import render,redirect
from .forms import statusform
from .models import Status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User



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

def get_login_page(req):
    return render(req,"login.html")

def get_sign_up_page(req):
    return render(req,"sign_up.html")

def post_create_user(req):
    username=req.POST["username"]
    password=req.POST["password"]
    fname=req.POST["fname"]
    lname=req.POST["lname"]
    address=req.POST["address"]
    phonenumber=req.POST["phonenumber"]
    emailaddress=req.POST["emailaddress"]

    print(username)

    user=User.objects.create_user(username=username,email=emailaddress,password=password)

    user.save()

    return redirect("login")

def post_login_user(req):
    username=req.POST["username"]
    password=req.POST["password"]

    print(username,password)

    user=authenticate(username=username,password=password)
    print(user)
    if user is not None:
        return render(req,"home.html")
    else:
        return redirect("login")
    