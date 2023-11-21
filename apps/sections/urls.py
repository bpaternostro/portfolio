from rest_framework.routers import DefaultRouter
from .views.views import *

router = DefaultRouter()
router.register(r"person", PersonViewSet)
router.register(r"post", PostViewSet)
router.register(r"message", MessageViewSet)