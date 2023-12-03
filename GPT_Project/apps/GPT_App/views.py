from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from apps.LLM import get_completion


# Create your views here.



class ChatHistoryViewSet(ModelViewSet):
    queryset = ChatHistory.objects.all()
    serializer_class = ChatHistorySerializer


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by("-id"))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
## GPT3.5
    @action(detail=False, methods=['post'])
    def chat(self, request):
        data = request.data
        print("这是前端传过来的数据",data)


        user_input=data.get("message")

        chat_id=data.get("chat_id")

        option=data.get("option")

        chat_history= self.filter_queryset(self.get_queryset().get(id=chat_id))

        gpt_response = get_completion(ChatMessageSerializer(chat_history.messages.all(),many=True).data,user_input,option)

        
        chat_message = ChatMessage.objects.create(chat_history=chat_history, user_input=user_input, gpt_response=gpt_response)

        return Response(ChatMessageSerializer(chat_message).data)

    @action(detail=True,methods=["get"])
    def chat_messages(self,request,pk=None):
        chat=self.get_object()
        messages=ChatMessageSerializer(chat.messages.all(),many=True)
        return Response(messages.data)
