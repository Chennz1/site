from django.http import HttpResponse
from django.shortcuts import render
from sympy import re
from main.models import Course, Wangke
from main.models import models


# Create your views here.
def index(req):
    # if req.method == "GET":
    #     return render(req,"login_.html")
    # return render(req,"studyweb.html")
    if req.method == "GET":
        courses=Course.objects.all()
        wangkes=Wangke.objects.all()[:5]
        return render(req,"studyweb.html",{"courses":courses,"wangkes":wangkes})
    info=req.POST.get("info")
    courses=Course.objects.all()
    wangkes=Wangke.objects.filter(courseid==info)
    return render(req,"studyweb.html",{"courses":courses,"wangkes":wangkes})

# def login(req):
def course(req,nid):
    return render(req,"course。html",{"nid":nid})
    

# def dataoperation(req):
    #base.objects.create("id=value")
    #base.objects.filter("id=value").delete()
    #base.objects.all().delete()
    #querysite=base.objects.filter("id=value")
    #row=base.objects.filter(id=2).first()
    #row.id row... 
    #base.objects.filter(id=2).update(name=99)


    # return HttpResponse("end")