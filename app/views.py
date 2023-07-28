from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template
from django.template.loader import render_to_string
from app.models import Product

# Create your views here


def index(request):
    return render(request, "index.html", {})


def catalog(request):
    products = Product.objects.all()
    for product in products:
        product.image_list = list(map(lambda x: x.image, product.images.all()))

    rendered = render_to_string("catalog.html", {'products': products})
    return HttpResponse(rendered)


def schedule(request):
    return render(request, "schedule.html", {})


def location(request):
    return render(request, "location.html", {})
