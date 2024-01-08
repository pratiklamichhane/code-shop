from django.contrib import admin
from .models import Category , Product 

# Register your models here.
#new bug
admin.site.register(Category)
admin.site.register(Product)

