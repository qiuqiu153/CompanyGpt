
from django.contrib import admin
from apps.GPT_App.models import * 

# # Register your models here. 

class customChatHistory(admin.ModelAdmin):
    list_display = ('chat_name',"timestamp") # list
    search_fields = ('chat_name',)

admin.site.register(ChatHistory,customChatHistory)
admin.site.register(ChatMessage)