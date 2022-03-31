from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def home_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            messages.error(request, 'Please correct the errors below!')
    else:
        form = ContactForm(request.POST)

    return render(request, 'home.html', {'form': form})


def blog_home(request):
    return render(request, 'blog-base.html')