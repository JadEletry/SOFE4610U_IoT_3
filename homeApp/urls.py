from django.urls import include, path
from rest_framework.routers import DefaultRouter

from homeApp import views

# Create routers for mode and state viewsets
router = DefaultRouter() 
router.register(r'mode', views.ModeViewSet) 
router.register(r'state', views.StateViewSet) 

urlpatterns = [
    path("", views.homeApp, name="homeApp"),
    path('api/', include(router.urls)),

]