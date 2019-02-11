from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import Users_Form
from .models import Users,info
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'home.html',{})
def form_users(request):
    new = Users_Form(request.POST or None)
    obj = Users()
    if new.is_valid():
        obj.First_Name =new.cleaned_data['First_Name']
        obj.Last_Name  =new.cleaned_data['Last_Name']
        obj.Email      =new.cleaned_data['Email']
        obj.Birth_Day  =new.cleaned_data['Birth_Day']
        obj.save()
        return HttpResponseRedirect ('/home')
    return render(request,'form_users.html',{'f':new})
#######################################################
#                   Register                          #
#######################################################
def register(request):
    return render(request,'register.html',{})
def register_backend(request):
    try:
        new = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['password'])
        new.first_name=request.POST['first_name']
        new.last_name=request.POST['last_name']
        new.save()
        return HttpResponseRedirect ('/home')
    except:
        return HttpResponse('User Is Exist')
#######################################################
#                     Log in                          #
#######################################################
def log(request):
    return render(request,'login.html',{})
def profile(request,username):
    return render(request,'profile.html',{'u':username})
def log_backend(request):
    u = request.POST['username']
    p = request.POST['password']
    re=authenticate(username=u,password=p)
    if re is not None:
        print('Log In')
        login(request,re)
        link='/home/profile/'+str(re)
        return HttpResponseRedirect(link)
    else:
        return HttpResponse('User Is Not Exist')
#######################################################
#                     Log out                         #
#######################################################
def logout_backend(request):
    logout(request)
    return HttpResponse('log out')
#######################################################
#               table concet with tabel               #
#######################################################
def log_info(request,username):
    return render(request,'log_info.html',{'username':username})
def info_backend(request,username):
    u=info()
    user=User.objects.get(username=username)
    u.job=request.POST['jobs']
    u.lang=request.POST['lang']
    u.num=request.POST['num']
    u.username=user
    u.save()
    return HttpResponse('yes i do')
#######################################################
#                                                     #
#######################################################
def show(request,username):
    user = User.objects.get(username=username)
    inf = info.objects.filter(username=user)
    context={'user':user,'inf':inf}
    return render(request,'show.html',context)
