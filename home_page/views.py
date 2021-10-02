from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from home_page.models import contactus
from home_page.models import student
from home_page.models import destinations

# Create your views here.


def myfunction(request):
    return HttpResponse("hello world")


def intro(request, name, age):

    mydictionary = {
        "name": name,
        "age": age
    }
    return JsonResponse(mydictionary)


def home(request):

    return(render(request, "index.html"))


def packages(request):
    return(render(request, "products.html"))


def trek(request):
    return(render(request, "third.html"))


def seadiving(request):
    return(render(request, "fourth.html"))


def contact_us(request):
    if request.method == "POST":

        
        name1 = request.POST["name"]
        email1 = request.POST["email"]
        mobile1 = request.POST["mobile"]
        suggestions1 = request.POST["suggestions"]
        pincode1 = request.POST["pincode"]
        

        contact=contactus()
        contact.name=name1
        contact.email=email1
        contact.mobile=mobile1
        contact.suggestions=suggestions1
        contact.pincode=pincode1
        
        contact.save()
        return(render(request,"show_cred.html",{"details":name1}))

    contact1=contactus.objects.get(id=5)
    print(contact1)
    contact1.name="Piyush Madhav Chaudhari"
    contact1.save()
    print(contact1.name)
    return(render(request, "contact_us.html"))

def destination(request):
    
    dest=destinations.objects.filter(name="Mumbai")
    print(str(dest))
    return(render(request, "show_cred.html",{"destination":dest}))
    


def addition(request):
    return (render(request, "addition.html"))


