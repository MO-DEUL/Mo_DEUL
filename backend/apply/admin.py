from django.contrib import admin
from . import models


@admin.register(models.Apply)
class ApplyAdmin(admin.ModelAdmin):
    pass
