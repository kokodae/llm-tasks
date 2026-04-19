from langchain_community.chat_models.gigachat import GigaChat 
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain_core.output_parsers import StrOutputParser

model = GigaChat( 
credentials="!!!your_credentials!!!", 
scope="GIGACHAT_API_PERS", 
model="GigaChat",
verify_ssl_certs=False, 
) 
parser = StrOutputParser() 
 
user_input = input("Введите сообщение на английском: ") 
messages = [ 
    SystemMessage(content="Переведи следующее сообщение с английского на русский"), 
    HumanMessage(content=user_input), 
] 
 
result = model.invoke(messages) 
print("Перевод: " + parser.invoke(result)) 
