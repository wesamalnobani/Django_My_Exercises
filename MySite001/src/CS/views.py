from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
# Create your views here.

def home(request):
    return render (request,'Index.html',{ })
def page01(request):
    return render(request,'Python.html',{ })
def page02(request):
    return render(request,'C++.html',{ })
def page03(request):
    return render(request,'JavaScript.html',{ })
def test01(request):
    t = '''
    <html>
        <head>
            <title> python 3</title>
        </head>
             my name is wesam
        <body>
        </body>
    </hmml>
     '''
    return HttpResponse(t)
def test02(request,n1,n2):
    t = n1+n2
    return HttpResponse('the sum is '+str(t))
def test03(request,a,b):
    return HttpResponse(a+str(b))
def test04(request,a,b,c):
    return HttpResponse(a+str(b+c))
def create_user(request):
    return render(request,'Form_Users.html',{ })
def backend01(request):
    #from From_Users.html
    v1 = request.POST['name']
    v2 = request.POST['Email']
    v3 = request.POST['age']
    v4 = request.POST['date']
    new=models.users()
    new.fullname=v1
    new.email=v2
    new.age=v3
    new.birthday=v4
    new.save()
    return HttpResponseRedirect ('/CS/')
def update_user(request,id):
    return render (request,'update_user.html',{'id_user':id })
def backend02(request,id):
    old=models.users(id=id,fullname=request.POST['name'],email=request.POST['Email'],age=request.POST['age'],birthday=birthday)
    old.save()
    return HttpResponse('update_user')
def backend03(request,id):
    old=models.users(id=id,)
    old.delete()
    return HttpResponse('deleted Data')
def backend04(request): #not complete yet
    data=models.users.objects.all()
    return render(request)
