from django.urls import path,include
from rest_framework import routers
from .views import CustomUserViewSet

router = routers.DefaultRouter()
router.register('drfcustomuser',CustomUserViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
