from django.contrib import admin
from .models import Beverage
# Register your models here.


class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')


admin.site.register(Beverage, BeverageAdmin)
