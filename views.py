from django.shortcuts import render,redirect
from django.contrib.auth import login, logout ,authenticate
from django.contrib.auth.models import User
from . models import gallery,buy_art
from django.contrib import messages
def home(request):
    return render(request,'home.html')
def art_view(request):
    Gallery=gallery.objects.all()
    return render(request,'art.html',{'Gallery':Gallery})
def register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['Email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['confirm_password']
        select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def user_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def admin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def buy_view(request,pk):
    art=gallery.objects.get(id=pk)
    if buy_art.objects.filter(user=request.user,art=art).exists():
        return redirect('list')
    else:
        Cart = buy_art.objects.create(user=request.user,art=art)
        Cart.save()
        messages.success(request,'Succesfully Buyed')
        return redirect('art')
    return redirect('art')
def list_buyed(request):
    list=buy_art.objects.all()
    return render(request,'buyedlist.html',{"list":list})
def gallery_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        price = request.POST['price']
        data=gallery.objects.create(owner=request.user,title=title,description=description,image=image,price=price)
        data.save()
        messages.success(request,'saved sucessfully')
        return redirect('add_art')
    return render(request,'addart.html')