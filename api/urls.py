from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register("products", views.ProductsViewSet)
router.register("categories", views.CategoryViewSet)


urlpatterns = [
    path("", include(router.urls)),
]