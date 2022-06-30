from django.urls import path
from . import views

urlpatterns = [
    path('', views.geData),
    path('add/', views.addCoupon),
]