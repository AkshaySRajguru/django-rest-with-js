from django.shortcuts import render


def home(request):
    return render(request, 'frontend/list.html', {'name': 'Hello Akshay'})
