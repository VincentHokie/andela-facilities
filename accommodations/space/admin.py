from django.contrib import admin
from .models import Room, Occupant, Space

# Register your models here.
admin.site.register(Space)
admin.site.register(Room)
admin.site.register(Occupant)
