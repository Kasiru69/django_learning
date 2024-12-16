from django.shortcuts import render, HttpResponse
from .models import Student
from home import run_db

def index(request):
    x=request.GET
    run_db.student()
    #print("hello")
    return HttpResponse(f"this is {x['name2']} world")








