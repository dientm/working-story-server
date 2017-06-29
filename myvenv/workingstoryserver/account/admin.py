from django.contrib import admin

from .models import AvatarModel


@admin.register(AvatarModel)
class AvatarModel(admin.ModelAdmin):
    pass
