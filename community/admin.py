from django.contrib import admin
from . import models


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
