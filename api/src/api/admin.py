from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import EquipmentModel, EquipmentTypeModel


@admin.register(EquipmentModel)
class EquipmentAdmin(ModelAdmin): ...


@admin.register(EquipmentTypeModel)
class EquipmentTypeAdmin(ModelAdmin): ...
