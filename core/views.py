from django.shortcuts import render, redirect
from .models import *
from item.models import Category,Item

from .forms import SignupForm
from django.contrib.auth import logout
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    if request.user.is_authenticated:
        return render(request, 'core/index.html', {
            'categories': categories,
            'items': items,
        })
    else:
        return redirect('core:login')

def logout_view(request):
    logout(request)
    return redirect('core:login')
def contact(request):
    if request.method == 'POST':
        ContactModel.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], message=request.POST['message'])
    return render(request, 'core/contact.html')

def privacy(request):
    return render(request,'core/privacy.html')

def term_use(request):
    return render(request, 'core/term_use.html')

def about(requesst):
    return render(requesst, 'core/about.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm()

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })