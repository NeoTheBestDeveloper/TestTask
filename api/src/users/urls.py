from django.urls import path

from .controllers import UserLoginController, UserLogoutController, UserRegistrationController, FetchMeController

__all__ = [
    "urlpatterns",
]


urlpatterns = [
    path("", UserRegistrationController.as_view()),
    path("login/", UserLoginController.as_view()),
    path("logout/", UserLogoutController.as_view()),
    path("me/", FetchMeController.as_view()),
]
