from django.urls import path
from .views import home,test01,test02,test03,test04,page01,page02,page03,create_user,backend01,update_user,backend02,backend03

urlpatterns = [
    path('',home,name='Index'),
    path('Python/',page01,name='Python'),
    path('C++/',page02,name='C++'),
    path('JavaScript/',page03,name='JavaScript'),
    path('test01/', test01,name='test01'),
    path('test02/<int:n1>/<int:n2>',test02,name='test02'),
    path('test03/<str:a>/<int:b>',test03,name='test03'),
    path('test04/<str:a>/<int:b>/<int:c>',test04,name='test04'),
    path('Form_Users/',create_user,name='Form_Users'),
    path('backend01/',backend01,name='backend01'),
    path('update_user/<int:id>/',update_user,name='update_user'),
    path('backend02/<int:id>',backend02,name='backend02'),
    path('backend03/<int:id>',backend03,name='backend03'),
]
