from django.contrib import admin
from public_service.models import Pessoa

# Register your models here.
class Pessoas(admin.ModelAdmin):
    list_display = ('id','name', 'birth', 'e_mail', 'states', 'marital_status', 'average_wage', 'schooling', 'alive')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Pessoa, Pessoas)