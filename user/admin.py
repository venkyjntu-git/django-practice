from django.contrib import admin
from .models import Person,Student

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=('name','age') 
    list_filter=('age',)
    search_fields=('name',)
admin.site.register(Person,PersonAdmin)
admin.site.register(Student)