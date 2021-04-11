from rest_framework.routers import DefaultRouter

from .views import BoundaryViewset

router = DefaultRouter()

router.register(
    prefix="api/v1/boundaries", viewset=BoundaryViewset, basename="boundary"
)

urlpatterns = router.urls
