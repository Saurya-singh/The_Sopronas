from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Permission
from django.db.models import Q
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


    status_list=Status.objects.all()
    search_term= ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        status_list = status_list.filter(yourpost__icontains=search_term)

    context = {'status_list': Status.objects.all(), 'search_term': search_term}

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

def searchresults(request):
    query = request.POST['search']
    result = Status.objects.filter(Q(yourpost__icontains=query))
    Context = {'result': result}
    return render(request, 'searchlist.html', Context)



def get_login_page(req):
    return render(req,"login.html")

def get_sign_up_page(req):
    return render(req,"sign_up.html")

def post_create_user(req):
    username=req.POST["username"]
    password1=req.POST["password1"]
    password2=req.POST["password2"]
    fname=req.POST["fname"]
    lname=req.POST["lname"]
    emailaddress=req.POST["emailaddress"]

    if password1==password2:
        if User.objects.filter(username=username).exists():
                messages.info(req,'Username exists, Try another one')
                return render(req,'sign_up.html')

        elif User.objects.filter(email=emailaddress).exists():
                messages.info(req,'Email already in use')
                return render(req,'sign_up.html')    

        else:    
            user=User.objects.create_user(username=username,email=emailaddress,password=password1,)
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

    else:
        messages.info(req,'Password do not match')
        return render(req,'sign_up.html')

def post_login_user(req):
    username=req.POST["username"]
    password=req.POST["password"]
    user=authenticate(username=username,password=password)
    
    if user is not None:

        login(req,user)
        return redirect("home")
    else:
        messages.error(req, ' username or password error')
        return redirect("login")

def user_logout(req):
    logout(req) 
    return redirect('login')