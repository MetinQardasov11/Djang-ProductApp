from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_active', 'is_bestseller', 'selected_category']
    list_editable = ['is_active', 'is_bestseller']
    search_fields = ['name', 'price']
    readonly_fields = ['slug']
    list_filter = ['is_active', 'is_bestseller', 'categories']
    
    def selected_category(self, obj):
        html = '<ul>'
        for category in obj.categories.all():
            html += f'<li>{category.name}</li>'
        html += '</ul>'

        return mark_safe(html)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)