from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_app.views import CarViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# url-> http://localhost:8000/api/v1/cars/
