from django.shortcuts import render

def home_view(request, *args, **kwargs):
    context = {"home_active": "active"}
    return render(request, 'home.html', context)

def about_view(request, *args, **kwargs):
    context = {"about_active": "active"}
    return render(request, 'about.html', context)

def contact_view(request, *args, **kwargs):
    context = {"contact_active": "active"}
    return render(request, 'contact.html', context)