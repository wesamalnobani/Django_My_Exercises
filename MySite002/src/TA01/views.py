from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HOME(request):
    return render (request,'index02.html',{})
def python(request):
    return render (request,'python.html',{})
def django(request):
    return render (request,'django.html',{})
def cpp(request):
    return render (request,'c++.html',{})
def AI(request):
    return render (request,'AI.html',{})
def whithout_html(request):
    s='''
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <title>YouTaxPro</title>
      </head>
      <body>
        <h1>First test</h1>
        <h1>python with djangoproject</h1>
      </body>
    </html>
    '''
    return HttpResponse(s)
def test01(request,n1,n2):
    s=n1+n2
    return HttpResponse('The sum is '+str(s))
def test02(request,a,b):
    return HttpResponse(a+str(b))
def test03(request,a,b,c):
    return HttpResponse(a+str(b+c))
