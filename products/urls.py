from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.semantic_search.as_view()),
    path('<int:product_id>/' , views.product_services_view.as_view()),
]