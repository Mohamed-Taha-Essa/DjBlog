from django.contrib import admin

from . models import Posts
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =['title' , 'draft']
    list_filter =['draft']
    search_fields =['title']


admin.site.register(Posts,ProductAdmin)
