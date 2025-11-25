from django.urls import path
from . import views 

urlpatterns = [
    path('search/' , views.semantic_search.as_view()),
    path('products-list/' , views.product_services_view.as_view()),
    path('ai-assistant/' , views.AIShoppingAssistant.as_view()),
]