from django.shortcuts import render, HttpResponse
from datetime import datetime
from prep.models import Contact
from django.contrib import messages

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