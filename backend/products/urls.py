from django.urls import path

from .views import ProductTestView

urlpatterns = [
    path("", ProductTestView.as_view())
]