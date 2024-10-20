from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def index(req):
    return HttpResponse('HELLO WORLD')


def specific(request):
    return HttpResponse('this is the specific urls ')



def article(request,article_id):
    return render(request,'index.html',{'article_id':article_id})



