from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter



router = DefaultRouter()

router.register("products", views.ProductsViewSet)
router.register("categories", views.CategoryViewSet)
router.register("carts", views.CartViewSet)



product_router = NestedDefaultRouter(router, "products", lookup="product")
product_router.register("reviews", views.ReviewViewSet, basename="product-reviews")

cart_router = NestedDefaultRouter(router, "carts", lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename="cart-items")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(product_router.urls)),
    path("", include(cart_router.urls))
]