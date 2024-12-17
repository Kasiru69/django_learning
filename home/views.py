from django.shortcuts import render, HttpResponse
from .models import Student
from home import run_db

def index(request):
    x=request.GET
    run_db.student()
    data={
        'title':"Hello World",
        'name':[x['name'],x['name2'],x['name3'],x['name4']]
    }
    #print("hello")
    return render(request,'index.html',data)








