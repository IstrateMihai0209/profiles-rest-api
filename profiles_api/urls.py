from django.urls import path
from . import views

urlpatterns = [
    path('api-view', views.ApiView.as_view()),
]