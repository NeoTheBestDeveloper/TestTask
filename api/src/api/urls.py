from django.urls import path

from .controllers import EquipmentController, EquipmentControllerList

__all__ = [
    "urlpatterns",
]

urlpatterns = [
    path("equipment/", EquipmentControllerList.as_view()),
    path("equipment/<int:pk>.", EquipmentController.as_view()),
]
