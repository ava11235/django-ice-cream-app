from django.contrib import admin


from .models import Icecream, Order
# Register your models here.
#admin.site.register(Icecream) # because it's registered in the models.py
admin.site.register(Order)

