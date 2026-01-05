from django.contrib import admin
from .models import Experience, Bio

# Register your models here. (Old classic visualizer)
#admin.site.register(Experience)
#admin.site.register(Bio)

# This decorator tells Django how to display the list in the admin
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('name',)