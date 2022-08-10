from django.contrib import admin

from .models import Car,Review, Driver

# Register your models here.
admin.site.register(Car)
admin.site.register(Review)
admin.site.register(Driver)