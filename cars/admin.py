from django.contrib import admin

# Register your models here.
from .models import ContactRequest, Car, Review, Order

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'price', 'discount', 'get_discounted_price')
    list_editable = ('price', 'discount')
    search_fields = ('name', 'engine')
    list_filter = ('year', 'color')
    
    def get_discounted_price(self, obj):
        return f"${obj.get_discounted_price():.2f}"
    get_discounted_price.short_description = 'Цена со скидкой'

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at')
    search_fields = ('name', 'phone')
    list_filter = ('created_at',)

admin.site.register(Review)
admin.site.register(Order)