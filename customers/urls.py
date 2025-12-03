from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CustomerProfileView, customer_wishlist_view
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', CustomerProfileView.as_view(), name='customer_profile'),
    path('wishlist/', customer_wishlist_view.as_view(), name='customer_wishlist'),
]