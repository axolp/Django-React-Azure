from django.contrib import admin
from api.models import fiszka

class AdminFiszka(admin.ModelAdmin):
    pass

admin.site.register(fiszka, AdminFiszka)

