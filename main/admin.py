from django.contrib import admin
from main.models import Item

class ItemAdmin(admin.ModelAdmin):
	list_display = ('device', 'imei', 'pub_date')
	list_filter = ['pub_date']
	search_fields = ['imei']
	date_hierarchy = 'pub_date'
	
admin.site.register(Item, ItemAdmin)