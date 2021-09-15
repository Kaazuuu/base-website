from django.urls import path
from .views import indexView

urlpatterns = [
    path('', IndexView.as_view()),
    ]