from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.semantic_search.as_view()),
    # path('search/' , views.product_viewset.as_view({'get':'list'}))
]