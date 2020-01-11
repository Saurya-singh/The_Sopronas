from django.shortcuts import render

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
    return render(request, "./status_list.html")

def status_form(request):
    return render(request, "./home.html")

def status_delete(request):
    return 