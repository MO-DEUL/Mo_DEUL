from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name", "description", "city", "address", "price"
            ),
        }),
    )


@admin.register(models.HouseType)
class TypeAdmin(admin.ModelAdmin):
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
