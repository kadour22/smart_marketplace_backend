from django.urls import path
from . import views
urlpatterns = [
    path('conversations/', views.ConversationListCreateView.as_view(), name='conversation-list-create'),
    path('messages/<int:conversation_id>/' , views.ConversationMessagesListCreate.as_view())
]