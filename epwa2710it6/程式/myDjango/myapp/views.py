from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def hello(request):
    return HttpResponse("hello Django")

def hello01(request,username):
    return HttpResponse("hello~:"+username)

def hello02(request, username):
    now=datetime.now()
    return render(request,"hello02.html", locals())
