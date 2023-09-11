from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'halaman':'Produk',
        'website':'Perpustakaan'
    }
    return render(request, 'index.html', context)