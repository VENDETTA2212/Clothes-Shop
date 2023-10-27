from django.urls import path
from .views import RegisterLoginView, HomeView


urlpatterns = [
    path('login/', RegisterLoginView.as_view(), name='LR'),
    path('profile/', HomeView.as_view()),
]