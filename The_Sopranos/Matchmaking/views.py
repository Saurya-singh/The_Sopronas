from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from .forms import statusform
from .models import Status

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def notification(request):
    return render(request, 'notification.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='login')
def search(request):
    return render(request, 'search.html')


@login_required(login_url='login')
def status_list(request):
    context = {'status_list': Status.objects.all()}
    return render(request, "./status_list.html", context)


@login_required(login_url='login')            
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

     #user permission 
    content_type=ContentType.objects.get_for_model(Status)

    #add permission
    permission=Permission.objects.get(
        codename='add_status',
        content_type=content_type
    )

    user.user_permissions.add(permission)
    
    #view permission
    permission=Permission.objects.get(
        codename='view_status',
        content_type=content_type
    )

    user.user_permissions.add(permission)    


    login(req,user)

    return redirect("home")

def post_login_user(req):
    username=req.POST["username"]
    password=req.POST["password"]

    print(username,password)

    user=authenticate(username=username,password=password)
    print(user)
    if user is not None:

        login(req,user)
        return redirect("home")
    else:
        messages.error(req, 'Bad username or password')
        return redirect("login")

def user_logout(req):
    logout(req) 
    return redirect('login')
    