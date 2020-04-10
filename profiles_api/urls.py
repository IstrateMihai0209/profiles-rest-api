from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('view-set', views.Viewset, basename='view-set')

urlpatterns = [
    path('api-view', views.ApiView.as_view()),
    path('', include(router.urls)),
]