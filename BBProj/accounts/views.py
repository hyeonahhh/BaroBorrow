from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from accounts import views as account_views

# Create your views here.
def login(request):
    if request.method == 'POST':
       username =  request.POST['username']
       password = request.POST['password']
       name = request.POST['name']
       nickname = request.POST['nickname']
       location_city = request.POST['location_city']
       location_gu = request.POST['location_gu']
       user = auth.authenticate(request, username=username, password=password, name=name, nickname=nickname, location_city=location_city, location_gu=location_gu)

       if user is not None:
           auth.login(request, user)
           return redirect()
       else:
            return render(request, )
    else:
        return render(request, )

def signup(request):
    if request.method == "POST":
        if request.POST['password']== request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], name=request.POST['name'], nickname=request.POST['nickname'], location_city=request.POST['location_city'], location_gu=request.POST['location_gu'])
            auth.login(request, new_user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect()
    return render(request,)

def logout(request):
   auth.logout(request)
   return render(request, )