from django.contrib import admin
from . import models


@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):
    pass


@admin.register(models.HouseType)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
