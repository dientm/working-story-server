from django.contrib import admin
from worklog.models import WorkLog, LocalBeacon

@admin.register(WorkLog)
class WorkLog(admin.ModelAdmin):
    pass

@admin.register(LocalBeacon)
class LocalBeacon(admin.ModelAdmin):
    pass