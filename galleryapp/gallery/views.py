from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    images = Pic.objects.all()
    if request.GET.get('search'):
        images = images.filter(Name__icontains = request.GET.get('search')) 
    return render(request,'home.html',{'images':images})

@login_required(login_url='/login/')
def add(request):
    if request.method == "POST":
        Pic.objects.create(
            Name = request.POST.get('name'),
            Image = request.FILES.get('image')
        )
        messages.success(request, "Photo Added Succesfully")
        return redirect('/')
    return render(request,'add.html')

@login_required(login_url='/login/')
def delete(request,id):
    Pic.objects.get(id=id).delete()
    messages.info(request, "Photo Deleted Successfully")
    return redirect('/')



def login_page(request):
    if request.method == "POST":
        data = request.POST
        if not User.objects.filter(username = data.get('user_name')).exists():
            messages.warning(request, "Username is does not exist")
            return redirect('/login/')
        user = authenticate(username = data.get('user_name'), password = data.get('password'))
        if user is None:
            messages.warning(request, "Password does not match")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html') 


def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        data = request.POST
        if User.objects.filter(username = data.get('user_name')).exists():
            messages.warning(request, "Username already exist")
            return redirect('/register/')

        if  (data.get('password') != data.get('confirm_password')):
            messages.warning(request, "Password and confirm Password does not match")
            return redirect('/register/')

        reg = User.objects.create(
                username = data.get('user_name')
            )    
        reg.set_password(data.get('password'))
        reg.save()
        return redirect('/login/')
    return render(request,'register.html') 