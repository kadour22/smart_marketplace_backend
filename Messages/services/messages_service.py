from rest_framework.response import Response
from rest_framework import status

from django.db.models import Q
from django.db import transaction

from Messages.models import Message , Conversation
from Messages.serializers import (
    conversationSerializer,
    messageSerializer,
    sendMessageSerializer
    )

# conversation list logic
def get_conversations_list(sender , recipient) :
    conversations = Conversation.objects.select_related(
            "product" , "sender","recipient"
        ).filter(
            Q(sender = sender) | Q(recipient=recipient)
        ).all()
    
    serializer = conversationSerializer(conversations, many=True)
    return Response(serializer.data)

# create conversation logic
def initiate_conversation(sender,data):
    serializer = conversationSerializer(data=data)
    if serializer.is_valid():
        serializer.save(sender=sender)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# conversation messages logic 
def conversation_messages_list(conversation_id):
    try:
            conversation = Conversation.objects.get(id=conversation_id)
    except Conversation.DoesNotExist:
            return Response({"error": "Conversation not found"}, status=status.HTTP_404_NOT_FOUND)
        
    messages = Message.objects.filter(
            conversation__id=conversation_id
        ).select_related(
            "conversation", "sender"
        ).all()

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

# sending message logic
def sending_message(data,sender) :
    print("Request data:", data)  
    serializer = sendMessageSerializer(data=data)
    if serializer.is_valid():
        with transaction.atomic():
            message = serializer.save(sender=sender)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)