from django.urls import path
from . import views

urlpatterns = [
    path("", views.variable01),
    path("var01/", views.variable01),
]