from django.urls import path
from . views import show_data,create_user,backend01,update_user,backend02,delete_user,upload_img

urlpatterns = [
    path('',show_data),
    path('user/',create_user,name='create_user'),
    path('backend01/',backend01,name='backend01'),
    path('update_user/<int:id>/', update_user,name='update_user'),
    path('backend02/<int:id>/', backend02, name='backend02'),
    path('user_deleted/<int:id>/',delete_user,name='delete_user'),
    path('upload_img/',upload_img,name='upload_img')
]
