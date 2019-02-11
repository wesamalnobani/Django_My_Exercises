"""Tax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TA01.views import HOME,whithout_html,test01,test02,test03,AI,cpp,python,django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HOME,name='index02'),
    path('ArtificialIntelligence/',AI,name='AI'),
    path('C++/',cpp,name='cpp'),
    path('Python/',python,name='python'),
    path('django/',django,name='django'),
    path('html/',whithout_html,name='html'),
    path('test01/<int:n1>/<int:n2>',test01,name='t01'),
    path('test02/<str:a>/<int:b>',test02,name='t02'),
    path('test03/<str:a>/<int:b>/<int:c>',test03,name='t03'),
]
