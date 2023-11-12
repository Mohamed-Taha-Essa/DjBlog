from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin


from . models import Post, Category,Comment
# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    list_display =['title' , 'draft']
    list_filter =['draft']
    search_fields =['title']
    summernote_fields = ('content',)



admin.site.register(Post,ProductAdmin)
admin.site.register(Comment)
admin.site.register(Category)
