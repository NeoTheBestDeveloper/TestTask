from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Equipment, EquipmentType


@admin.register(Equipment)
class EquipmentAdmin(ModelAdmin): ...


@admin.register(EquipmentType)
class EquipmentTypeAdmin(ModelAdmin): ...
