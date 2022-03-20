from django.shortcuts import render
# Create your views here.  
from django.http import HttpResponse  
# Importing datetime module
import datetime as dt
from datetime import datetime

from app.functions.functions import handle_uploaded_file  
from app.forms import StudentForm  
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return read_file(request,request.FILES['file']) 
    else: 
        student = StudentForm()  
        return render(request,"index.html",{'form':student})  

def read_file(request,fn):
    f = open('app/static/upload/'+fn.name, 'r',encoding="utf8")
    file_content = f.read()
    f.close()
    lines = file_content.split('\n')
    context = lines
    # context = file_content

    return render(request, "test2.html", {'context':context})