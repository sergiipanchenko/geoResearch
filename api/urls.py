from rest_framework import routers

from .views import PolyViewSet


router = routers.DefaultRouter()
router.register(r'polygons', PolyViewSet)

urlpatterns = router.urls
