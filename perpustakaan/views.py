from django.shortcuts import render

def index(request):
    context = {
        'halaman':'Beranda',
        'website':'Perpustakaan'
    }
    return render(request, 'index.html', context)