from django.urls import path
from . import views

from django.contrib import admin  
# aboove: no need here but to run code to see home html page i added this here
# if ntg is in urls file it show error hence added this for now

urlpatterns = [
    path('admin/', admin.site.urls),
]
