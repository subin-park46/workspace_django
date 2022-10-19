from django.urls import path
from . import views

urlpatterns = [
    path("", views.index), # 아무것도 없이 들어오면 views.index 호출
    path("test/", views.test)
]
