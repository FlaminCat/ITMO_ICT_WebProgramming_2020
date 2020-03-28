from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('owner/<int:driver_id>', views.get_driver),
        path('auto/<int:auto_id>', views.CarView.as_view())
]
