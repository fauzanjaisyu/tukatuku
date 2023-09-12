from django.shortcuts import render

# Create your views here.

def show_stock(request):
    context = {
        'name': 'Buku Tulis SIDU',
        'amount': 20,
        'description' : 'Buku tulis sekolah merk SIDU',
        'price' : 5000,
        'category' : 'Book'
    }

    return render(request, "main.html", context)