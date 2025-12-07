from django.urls import path
from . import views

urlpatterns = [
    path('conversations/', views.ConversationListCreateView.as_view(), name='conversation-list-create'),
    path('messages/<int:conversation_id>/' , views.ConversationMessagesList.as_view()),
    path('send/message/' , views.SendMessage.as_view()),
]