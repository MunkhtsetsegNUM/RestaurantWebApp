from django.contrib import admin
from blog.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'rate', 'author_id']
    readonly_fields = ['author']
# Register your models here.
