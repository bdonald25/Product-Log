from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template import RequestContext, loader
from products.models import Product

def products(request):
    template = loader.get_template('products/products.html')
    context = RequestContext(request)

    product_list = Product.objects.all()

    context = RequestContext(request, {
        'products': product_list,
    })

    return HttpResponse(template.render(context))