from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable1':"my name is shivam",
        'variable2':"this is my learning",
        'variable3':"i am start learing django"

    }
    
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is About")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Message Sent !')

    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")