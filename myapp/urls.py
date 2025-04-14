from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[

    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('logint',views.logint,name='logint'),
    path('mainpage/inputform',views.inputform,name='inputform'),
    path('mainpage/storeinput',views.storeinput,name='storeinput'),
    path('mainpage/inputcoursecode',views.inputcoursecode,name='inputcoursecode'),
    path('mainpage/updatecoursecode',views.updatecoursecode,name='updatecoursecode'),
   #  path('mainpage/mainpage/updatecoursecode',views.updatecoursecode,name='updatecoursecode'),
    path('mainpage/viewplan',views.viewplan,name='viewplan'),
    path('mainpage/updateplan',views.updateplan,name='updateplan'),
    path('mainpage/updateinput',views.updateinput,name='storeinput'),
    path('mainpage/<str:name>',views.mainpage,name='mainpage'),
    ############################new project updates
    path("uploadpdf", views.upload_pdf, name="upload_pdf"),
    path('mainpage/uploadpdf', views.upload_pdf, name="upload_pdf"),
    
]
urlpatterns += staticfiles_urlpatterns()
