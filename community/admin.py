from django.contrib import admin
from . import models


@admin.register(models.Community)
class CommunityAdmin(admin.ModelAdmin):


    list_filter = ('post',)

    list_display = ('title',
                    'writer',
                    'post',
                    'time',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_filter = ('time',)

    list_display = ('title',
                    'writer',
                    'comment',
                    'time',)
