from django.urls import path
from .views import home,form_users,register,register_backend,log,log_backend,profile,logout_backend,log_info,info_backend,show

urlpatterns = [
    path('',home),
    path('form_users/',form_users),
    path('register/',register,name="register"),
    path('register_backend/',register_backend,name="register_backend"),
    path('log/',log),
    path('log_backend/',log_backend,name='log_backend'),
    path('profile/<str:username>/',profile,name="profile"),
    path('logout_backend/',logout_backend,name='logout_backend'),
    path('log_info/<str:username>/',log_info),
    path('info_backend/<str:username>/',info_backend,name='info_backend'),
    path('show/<str:username>',show,name='show'),
]
