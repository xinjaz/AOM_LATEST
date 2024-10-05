from django.shortcuts import render, redirect

from item.models import Category,Item

from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
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