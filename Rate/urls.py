from django.urls import path
from . import views

urlpatterns = [
    path('rate-seller/', views.rate_seller_view.as_view()),
] 