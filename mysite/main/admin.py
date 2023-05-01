from django.contrib import admin
from .models import AboutUs, MenuFood, Book, Contact
# Register your models here.


admin.site.register(AboutUs)


@admin.register(MenuFood)
class MenuFoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'price']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'email']