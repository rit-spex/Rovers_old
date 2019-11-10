from django.contrib import admin
from .models import Rover_Base_Station # add this

class Rover_Base_Station_Admin(admin.ModelAdmin):  # add this
    list_display = ('title', 'description', 'completed') # add this

# Register your models here.
admin.site.register(Rover_Base_Station, Rover_Base_Station_Admin) # add this