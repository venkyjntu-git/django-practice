from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
def helloworld(request,number):
    persons=Person.objects.all()
    return render(request,"hello.html",{'number':number,'persons':persons})

def store_person(request):
    if request.method == "POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        Person.objects.create(name=name,age=age)
        persons=Person.objects.all()
        return render(request,"hello.html",{'persons':persons})