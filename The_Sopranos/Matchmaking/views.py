from django.shortcuts import render
#from .models import User
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
def upload(request):
    uploaded_file = ''
    if request.method == 'POST':
        uploaded_file = request.FILES['image']
    #user = User(pic = uploaded_file);
    #user.save();
    return render(request, 'uploadapp.html', {'file': uploaded_file})