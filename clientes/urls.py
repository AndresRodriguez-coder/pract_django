from rest_framework.routers import DefaultRouter
from .views import ClienteViewset

router = DefaultRouter()

router.register(r'', ClienteViewset, basename='Clientes')

urlpatterns = router.urls
