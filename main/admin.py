# Admin.py Handwritten by google.com/+Nkansahrexford
from django.contrib import admin
from main.models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('device', 'slug', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['slug']
	date_hierarchy = 'pub_date'
	
admin.site.register(Item, ItemAdmin)