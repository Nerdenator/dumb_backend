from django.conf.urls import url, include
from rest_framework import routers
from .views import DumbViewSet

router = routers.DefaultRouter()
router.register(r'dumb', DumbViewSet)

