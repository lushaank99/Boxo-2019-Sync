from django.contrib import admin
from .models import comments_list

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'comment')
admin.site.register(comments_list, CommentAdmin)