from django.contrib import admin
from . models import Stock  # need to import stock class from models

# this will add a section in localhost:8000/admin page for new database
admin.site.register(Stock)  # registers new Stock class model from Models file
