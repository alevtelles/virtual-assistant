from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AssistenteViewSet, DocumentoViewSet

router = DefaultRouter()
router.register(r'assistentes', AssistenteViewSet)
router.register(r'documentos', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
