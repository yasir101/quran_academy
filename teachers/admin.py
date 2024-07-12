from django.contrib import admin
from . import models

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email' ]

    def full_name(self, obj):
        return str(obj)

admin.site.register(models.Teacher, TeacherAdmin)