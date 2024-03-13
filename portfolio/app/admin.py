from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import *

# Define the inline class
class PortfolioImagesInline(admin.TabularInline):
    model = PortfolioImages
    extra = 1

# Register your models with the inline class
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = (PortfolioImagesInline,)

@admin.register(PortfolioImages)
class PortfolioImagesAdmin(admin.ModelAdmin):
    pass

# Register the rest of your models
admin.site.register(AboutMe)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Contact)