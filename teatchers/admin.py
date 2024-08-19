from django.contrib import admin
from . models import Teachers
# Register your models here.
@admin.register(Teachers)
# @admin.site.register(Students)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject', 'gender']