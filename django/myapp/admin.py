from django.contrib import admin

# Register your models here.
from .models import Person

class PersonAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'location', 'add_date', 'num_stars', 'sizes')
    list_filter = ('num_stars', 'sizes')
    search_fields = ('id', 'name', 'location', 'add_date', 'num_stars', 'sizes')


admin.site.register(Person, PersonAdmin)
