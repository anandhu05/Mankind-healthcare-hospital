from django.contrib import admin

from .models import departments,doctors,booking
# Register your models here.

admin.site.register(departments)
admin.site.register(doctors)
admin.site.register(booking)