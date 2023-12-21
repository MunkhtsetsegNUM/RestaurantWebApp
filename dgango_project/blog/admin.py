from django.contrib import admin
from blog.models import Review

# Админ интерфэйс дээр энэ талбарыг зөвхөн уншигдахуйц байдлаар харуулах ёстойг харуулж байна.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'rate', 'author_id']
    readonly_fields = ['author']

