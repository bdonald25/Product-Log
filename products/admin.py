from django.contrib import admin
from products.models import Product

# This file determines what you can see on the admin page. (/admin)

admin.site.register(Product)