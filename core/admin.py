from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Product

# Register your models here.


@admin.register(Customer)
class Customer(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'department')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'department')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('department',)}),
    )

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description', 'price')