from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation, Message
from .serializers import conversationSerializer, messageSerializer, sendMessageSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.db.models import Q
class ConversationListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
    
        conversations = Conversation.objects.select_related(
            "product" , "sender","recipient"
        ).filter(
            Q(sender = request.user) | Q(recipient=request.user)
        ).all()
    
        serializer = conversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = conversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConversationMessagesList(APIView):
    def get(self, request, conversation_id):
        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)
        
        messages = Message.objects.filter(
            conversation__id=conversation_id
        ).select_related(
            "conversation", "sender"
        ).all()

        # Include conversation participants info
        data = {
            "conversation": {
                "id": conversation.id,
                "sender": conversation.sender.username,
                "recipient": conversation.recipient.username,
                "product": conversation.product.id
            },
            "messages": messageSerializer(messages, many=True).data
        }
        
        return Response(data, status=status.HTTP_200_OK)
class SendMessage(APIView):
    def post(self, request):
        print("Request data:", request.data)  
        serializer = sendMessageSerializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
               message = serializer.save(sender=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)