from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests

def home(request):

    response_cat = requests.get('https://api.thecatapi.com/v1/images/search').json()
    random_cat = response_cat[0]['url']

    response_weather = requests.get('https://api.openweathermap.org/data/2.5/weather?&units=imperial&lat=13.632186&lon=123.224565&appid=00421149d089b15c750a0745fb619766').json()
    current_weather = {
        'temperature' : response_weather['main']['temp'],
        'description' : response_weather['weather'][0]['description'],
        'icon' : response_weather['weather'][0]['icon'],
    }
    

    context = {'random_cat' : random_cat, 'current_weather' : current_weather }
    return render(request, 'main/home.html', context)

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}

    return render(request, 'main/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def portfolio(request):
    context = {}
    return render(request, 'main/portfolio.html')

def blog(request):
    blogs = Blog.objects.order_by('-blog_posted').all()

    if request.method == 'POST':                            #create/post a blog
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog')

    else:
        form = BlogForm()

    context = {'blogs': blogs, 'form': form}

    return render(request, 'main/blog.html', context)

def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogForm(instance=blog)
        
    context = {'form': form }
    return render(request, 'main/updateBlog.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == "POST":
        blog.delete()
        return redirect('blog')

    context = {'blog': blog }
    return render(request, 'main/delete_blog.html', context)

def code(request):
    codes = Code.objects.order_by('-code_posted').all()

    if request.method == 'POST':
        form = CodeForm(request.POST)

        if form.is_valid():
            form.save()
            new_code = Code.objects.order_by('-code_posted').first()
            return redirect('view_code', new_code.id)
    else:
        form = CodeForm()

    context = {'codes': codes, 'form': form }
    
    return render(request, 'main/code.html', context)

def view_code(request, pk):
    codes = Code.objects.all()
    codeList = codes.get(id=pk)

    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_code')
    else:
        form = CodeForm()

    context = {'codeList': codeList }
    
    return render(request, 'main/view_code.html', context)

def update_code(request, pk):
    code = Code.objects.get(id=pk)

    if request.method == 'POST':
        form = CodeForm(request.POST, instance=code)
        if form.is_valid():
            form.save()
            return redirect('view_code', pk)
    else:
        form = CodeForm(instance=code)
        
    context = {'form': form }
    return render(request, 'main/update_code.html', context)

def delete_code(request,pk):
    code = Code.objects.get(id=pk)

    if request.method == "POST":
        code.delete()
        return redirect('code')

    context = {'code': code }
    return render(request, 'main/update_code.html', context)
