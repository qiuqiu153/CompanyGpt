from rest_framework.serializers import *
from .models import ChatHistory, ChatMessage

class ChatMessageSerializer(ModelSerializer):
    class Meta:
        model = ChatMessage
        exclude=["chat_history"]

class ChatHistorySerializer(ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ["chat_name","id"]
