from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.sections.urls import router as person_router
#from apps.core.urls import urlpatterns as core_urls


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.registry.extend(person_router.registry)

app_name = "api"
urlpatterns = router.urls # + core_urls
