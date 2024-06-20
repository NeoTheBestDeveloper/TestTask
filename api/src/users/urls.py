from django.urls import path

from .controllers import UserLoginController, UserRegistrationController

__all__ = [
    "urlpatterns",
]


urlpatterns = [
    path("", UserRegistrationController.as_view()),
    path("login/", UserLoginController.as_view()),
]
