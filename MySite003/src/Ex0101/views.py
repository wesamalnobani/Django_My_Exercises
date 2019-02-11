from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from . import forms
# Create your views here.
'''
def firstHttp(request):
    return HttpResponse ('hello database MySQL')
'''
def show_data(request):
    show=models.Person_User.objects.all()
    return render(request,'home.html',{'data': show})
def create_user(request):
    return render(request,'form_new_user.html',{})
def backend01(request):
    new=models.Person_User(
    Full_Name=request.POST["Full_Name"],
    Email=request.POST["Email"],
    Age=request.POST["Age"],
    Birth_Day=request.POST["Birth_Day"])
    new.save()
    #return HttpResponse('Inserted Data')
    #return render(request,'form_new_user.html',{})
    return HttpResponseRedirect('/home')
def update_user(request,id):
    data=models.Person_User.objects.get(id=id)
    return render(request,'form_update_user.html',{'id_user':id,'d':data})
def backend02(request,id):
    old=models.Person_User(
    id=id,
    Full_Name=request.POST["Full_Name"],
    Email=request.POST["Email"],
    Age=request.POST["Age"],
    Birth_Day=request.POST["Birth_Day"])
    old.save()
    #return HttpResponse('Update Data')
    return HttpResponseRedirect('/home')
def delete_user(request,id):
    old=models.Person_User(id=id)
    old.delete()
    #return HttpResponse('user deleted')
    return HttpResponseRedirect('/home')
def upload_img(request):
    u = models.pic()
    f = forms.Pic_Form(request.POST, request.FILES)
    if f.is_valid():
        u.Name_Pic=f.cleaned_data['Name_Pic']
        u.Image   =f.cleaned_data['Image']
        u.save()
        return HttpResponse('Image Uploaded Thanks')
    return render(request,'pic.html',{'form':f})
