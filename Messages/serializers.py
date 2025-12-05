from rest_framework import serializers
from .models import Conversation, Message

class conversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id","sender", "recipient", "product"]
        read_only_fields = ["sender"]

class messageSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ["conversation", "sender", "content", "timestamp"]
        read_only_fields = ["conversation", "sender"]

    def get_sender(self , obj) :
        return obj.sender.username