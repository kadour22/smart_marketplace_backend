from django.urls import path
from . import views 

urlpatterns = [
    # product urls
    path('products-list/' , views.product_services_view.as_view()),
    path('product/<int:product_id>/' , views.product_detail_view.as_view()),
    path('delete-product-from-wishlist/<int:product_id>/' , views.DeleteProductFromWishlistView.as_view()),
    # ai and search urls
    path('search/' , views.semantic_search.as_view()),
    path('ai-assistant/' , views.AIShoppingAssistant.as_view()),
    # wishlist urls
    path('wishlist/<int:product_id>/' , views.WishlistServiceView.as_view()),
    path('compare-product/' , views.compare_products_view.as_view())
]