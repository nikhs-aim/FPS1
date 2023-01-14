from django.contrib import admin
from .models import Conference,Journal

# Register your models here.

admin.site.register(Conference)
admin.site.register(Journal)