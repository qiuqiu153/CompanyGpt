
import openai
openai.api_key = "your_api_key"
proxy = {
'http': 'http://localhost:59527',
'https': 'http://localhost:59527'
}
openai.proxy = proxy


def get_completion(history, user_input,option)->str:
        message_produce_function=None
        if option=="CompanyGPT":
            message_produce_function=gpt
        elif option=='CompanySpark':
             message_produce_function=spark
       
        elif option=="向量数据库":
             message_produce_function=faiss
        else:
             return KeyError("option值异常")

        return message_produce_function(history, user_input)
def gpt(history, user_input,model="gpt-3.5-turbo")->str:
    """
        使用 OpenAI 的模型生成聊天回复。

        参数:
        model: 使用的模型，默认为"gpt-3.5-turbo"。
    """
    
    messages=get_messages_list(history,user_input)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )


    print(response)
    return response.choices[0].message["content"] # 模型生成的回复
def spark(history,user_input)->str:
     messages=get_messages_list(history,user_input)
     return "spark"
def faiss(history,user_input)->str:
     messages=get_messages_list(history,user_input)
     return "faiss"
def get_messages_list(history,user_input)->list:
    messages = []

    for i in history:
        messages.append({"role":"user","content":i["user_input"]})
        messages.append({"role":"assistant","content":i["gpt_response"]})



    messages.append({"role":"user","content":user_input})
    print(messages)

    return messages
    
