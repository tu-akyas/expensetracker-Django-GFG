from django.contrib import admin
from .models import CurrentBalance, TrackingHistory

# Register your models here.

admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory)