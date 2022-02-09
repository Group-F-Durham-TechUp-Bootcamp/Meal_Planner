from django.urls import path

from . import views

urlpatterns = [
    path('security', views.security),
    path('authorised', views.authorised),
]