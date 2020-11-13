from django.urls import path

from .views import ResisterView, LoginView

urlpatterns = [
    path('register/', ResisterView.as_view()),
    path('login/', LoginView.as_view()),
]