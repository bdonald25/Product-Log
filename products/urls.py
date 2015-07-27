from django.conf.urls import patterns, include, url

from products import views

# This file contains urs. Typically when a user goes to a url a method in the view.py
# file will be run and then data will be passed from their to a template file. 
# A template file is html with embeded python.

urlpatterns = patterns('',

    # ex: localhost:8000/
    url(r'^$', views.products, name='products'),

)