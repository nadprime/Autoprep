from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from prep.models import Contact
from django.contrib import messages
#from .models import FileModel, ImageModel
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from . models import myuploadfile
#from django.core.files.storage import FileSystemStorage
#from prep.models import Unstructured

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
    context = {
        "data":myuploadfile.objects.all(),
    }
    return render(request,"unstructured.html",context)

def send_files(request):
    if request.method == "POST" :
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfiles")
        
        for f in myfile:
            myuploadfile(f_name=name,myfiles=f).save()
        
        
        return HttpResponse("Your File Has Been Successfully Uploaded!") 




    # if request.method == "POST":
    #     myfile = request.POST.get('myfile')
    #     unstructured = Unstructured(myfile=myfile)
    #     unstructured.save()
    #     messages.success(request, 'Your file has been sent')
    # if request.method == 'POST' and request.FILES['myfile']
       # myfile = request.FILES['myfile']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        # return render(request, 'core/unstructured.html', {
            # 'uploaded_file_url': uploaded_file_url
        # })
    # return render(request, 'core/simple_upload.html')
    return render(request, 'unstructured.html')
    # return HttpResponse("this is unstructured page")

def semistructured(request):
    return render(request, 'semistructured.html')
    # return HttpResponse("this is semistructured page")

def structured(request):
    return render(request, 'structured.html')
    # return HttpResponse("this is ustructured page")


# def single_upload(request):
#     file = request.FILES.get("file")
#     FileModel.objects.create(file=file)
#     return JsonResponse({"message": "success"})

# def multiple_upload(request):
#     files = request.FILES.getlist("files")
#     files_list = []
#     for file in files:
#         files_list.append(FileModel(file=file))

#     if files_list:
#         FileModel.objects.bulk_create(files_list)

#     return JsonResponse({"message": "success"})    


#def simple_upload(request):
 #   if request.method == 'POST' and request.FILES['myfile']:
  #      myfile = request.FILES['myfile']
   #     fs = FileSystemStorage()
    #    filename = fs.save(myfile.name, myfile)
     #   uploaded_file_url = fs.url(filename)
      #  return render(request, 'core/simple_upload.html', {
       #     'uploaded_file_url': uploaded_file_url
        #})
    #return render(request, 'core/simple_upload.html')
