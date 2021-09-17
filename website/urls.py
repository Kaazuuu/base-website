from django.urls import path
from .views import IndexView, Article_1

urlpatterns = [
    path('', IndexView.as_view()),
    path('article_1/', Article_1.as_view()),
    ]