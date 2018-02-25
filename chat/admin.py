from django.contrib import admin
from .models import Basic_data, Additional_data

class Additional_dataInline(admin.TabularInline):
    model = Additional_data
    extra = 5

class Basic_dataAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,           {'fields': ['place_name','religion',
    'travel_expenses', 'hotel_expenses', 'info']}),
    ]
    inlines = [Additional_dataInline]


admin.site.register(Basic_data, Basic_dataAdmin)
