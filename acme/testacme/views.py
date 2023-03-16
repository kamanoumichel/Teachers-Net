from django.shortcuts import render
from django.http import HttpResponse,Http404
#from .mocks import Post
from .models import Post


# Create your views here.

#post=[]
def hello(request):
    post=Post.objects.all()
    return render(request,"home.html")
def blog(request):
    post=Post.objects.all()
    return render(request,"hello.html",{'toto':post})
    
def about(request):
    return render(request,"page/about.html")
def contact(request):
    return render(request,"page/contact.html")
def poste(request,id):
    try:
        post=Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("Sorry the post #{} was not found!!!".format(id))
    return render(request,"page/post.html",{'post':post})
def handler404(request):
    return render(request,'error/404.html',{},status=404)