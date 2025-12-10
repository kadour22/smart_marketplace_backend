from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services.messages_service import (
    get_conversations_list,
    initiate_conversation, 
    conversation_messages_list,
    sending_message
)

class ConversationListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        get_conversations_list(
            sender=request.user ,
            recipient=request.user
        )
        
    def post(self, request):
        initiate_conversation(
            data=request.data,
            sender=request.user
        )

class ConversationMessagesList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, conversation_id):
        conversation_messages_list(conversation_id=conversation_id)

class SendMessage(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        sending_message(data=request.data,sender=request.user)