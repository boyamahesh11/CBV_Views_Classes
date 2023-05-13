from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.

# Fbv returning a string

def Fbv_string(request):
    return HttpResponse('<center><h1>This is a Fbv</h1></center>')

# Cbv returning a string

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is a Cbv</h1>')

# Fbv return a htmlpage

def Fbv_html(request):
    return render(request,'Fbv_html.html')

# Cbv return a htmlpage

class Cbv_html(View):
    def get(self,request):
        return render(request,'Cbv_html.html')

# Fbv handling the forms

def Fbv_forms(request):
    tfo=TopicForm()
    d={'tfo':tfo}
    if request.method=="POST":
        tfd=TopicForm(request.POST)
        if tfd.is_valid():
            tfd.save()
            return HttpResponse('data is inserted_sucessfully')

    return render(request,'Fbv_forms.html',d)

# Cbv handling the forms

class Cbv_forms(View):
    def get(self,request):
        tfo=TopicForm()
        d={'tfo':tfo}
        return render(request,'Cbv_forms.html',d)
    def post(self,request):
        tfd=TopicForm(request.POST)
        if tfd.is_valid():
            tfd.save()
        return HttpResponse('data inserted sucessfully')

