from django.shortcuts import render
from django.shortcuts import HttpResponse
from propertyapp.models import Property
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, "profile.html")
        else:
            return render(request, 'signup.html', {'form': form})
            
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def index(request):
    propertys = Property.objects.all()
    if request.method == 'POST':
       usrname = request.POST['username']
       pwd =request.POST['password']
       user = authenticate(username=usrname , password=pwd)
       if user is not None:
        login(request,user)    
        return render(request,"profile.html", {"propertys": propertys, "user": user})
    
    return render(request, "main.html", {"propertys": propertys, "user": None})

def createproperty(request):
    newprop = Property()
    newprop.name = request.POST['name']
    newprop.description = request.POST['description']
    newprop.author = request.user
    newprop.price = request.POST['price']
    newprop.save()
    propertys = Property.objects.all()
    return render(request,"profile.html",{"propertys": propertys})

def editproperty(request): 
    if request.method=='GET':
        propid = request.GET.get('propid')
        return render(request,"editproperty.html",{"propid": propid})
    
    if request.method == 'POST':
         propid = request.GET.get('propid')
         user = request.user
         prop = Property.objects.get(id= propid)
         prop.name = request.POST['name']
         prop.description = request.POST['description']
         prop.author = request.user
         prop.price = request.POST['price']
         prop.save()
         propertys = Property.objects.all()
         return render(request,"profile.html",{"propertys": propertys,"user":user})

def deleteproperty(request):
    propid = request.GET.get('propid')
    prop = Property.objects.get(name= propid)
    prop.delete()
    propertys = Property.objects.all()
    return render(request,"profile.html",{"propertys": propertys})
    

    
    