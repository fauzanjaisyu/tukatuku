from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from main.models import MarketStock
from django.core import serializers
# Create your views here.

def show_stock(request):
    products = MarketStock.objects.all()

    context = {
        'name' : 'Muhammad Fauzan Jaisyurrahman',
        'class' : 'PBP - C',
        'products' : products,
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_stock'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = MarketStock.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MarketStock.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MarketStock.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MarketStock.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")