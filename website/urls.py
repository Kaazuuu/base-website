from django.urls import path
from .views import IndexView, Page1_1

urlpatterns = [
    path('', IndexView.as_view()),
    path('page1.1/', Page1_1.as_view()),
    ]