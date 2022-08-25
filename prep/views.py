from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from prep.models import Contact
from django.contrib import messages
from .models import FileModel, ImageModel
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")
    
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

def unstructured(request):
    return render(request, 'unstructured.html')
    # return HttpResponse("this is unstructured page")

def semistructured(request):
    return render(request, 'semistructured.html')
    # return HttpResponse("this is semistructured page")

def structured(request):
    return render(request, 'structured.html')
    # return HttpResponse("this is ustructured page")


def single_upload(request):
    file = request.FILES.get("file")
    FileModel.objects.create(file=file)
    return JsonResponse({"message": "success"})

def multiple_upload(request):
    file = request.FILES.getlist("files")
    files_list = []
    for file in files:
        files_list.append(FileModel(file=file))

    if files_list:
        FileModel.objects.bulk_create(files_list)

    return JsonResponse({"message": "success"})    



