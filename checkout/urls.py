from django.urls import path

from .views import checkout, checkout_success

urlpatterns = [
    path('', checkout),
    path('completed',checkout_success)
]