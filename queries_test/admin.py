from django.contrib import admin
from queries_test.models import student

# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'is_active', 'section','id']

admin.site.register(student, studentAdmin)