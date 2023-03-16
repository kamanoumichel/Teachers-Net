from django.urls import path
from django.conf.urls import handler404
from . import views

#handler404=views.handler404
urlpatterns = [
    path('',views.hello,name="hello"),
    path('blog/',views.blog,name="blog"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('post/<int:id>',views.poste,name="poste"),

]
