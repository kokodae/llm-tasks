from typing import Dict 
from langchain_gigachat.chat_models import GigaChat 
from langchain.tools import tool 
from langgraph.prebuilt import create_react_agent 
from langgraph.checkpoint.memory import MemorySaver 
import time 
orders_database = [ 
{ 
"order_id": "1", 
"customer_name": "Иван Иванов", 
"status": "Обработка",
"delivery_status": "Ожидает отправки", 
        "return_status": "Можно вернуть" 
    }, 
    { 
        "order_id": "2", 
        "customer_name": "Петр Петров", 
        "status": "Обработка", 
        "delivery_status": "Ожидает отправки", 
        "return_status": "Ожидает возврата" 
    }, 
    # Другие заказы... 
] 

# Функция для получения статуса заказа 
@tool 
def get_order_status(order_id: str) -> Dict: 
    """ 
    Возвращает статус заказа по его ID. 
 
    Args: 
        order_id (str): ID заказа. 
 
    Returns: 
        Dict: Словарь с информацией о статусе заказа. 
    """ 
    print("\033[92m" + f"Bot requested get_order_status({order_id})" + "\033[0m") 
    for order in orders_database: 
        if order["order_id"] == order_id: 
            return order 
    return {"error": "Заказ с таким ID не найден"} 

# Функция для получения статуса доставки 
@tool
def get_delivery_status(order_id: str) -> Dict: 
    """ 
    Возвращает статус доставки заказа по его ID. 
 
    Args: 
        order_id (str): ID заказа. 
 
    Returns: 
        Dict: Словарь с информацией о статусе доставки. 
    """ 
    print("\033[92m" + f"Bot requested get_delivery_status({order_id})" + "\033[0m") 
    for order in orders_database: 
        if order["order_id"] == order_id: 
            return {"delivery_status": order["delivery_status"]} 
    return {"error": "Заказ с таким ID не найден"} 

# Функция для получения статуса возврата 
@tool 
def get_return_status(order_id: str) -> Dict: 
    """ 
    Возвращает статус возврата заказа по его ID. 
 
    Args: 
        order_id (str): ID заказа. 
 
    Returns: 
        Dict: Словарь с информацией о статусе возврата. 
    """ 
    print("\033[92m" + f"Bot requested get_return_status({order_id})" + "\033[0m") 
    for order in orders_database: 
        if order["order_id"] == order_id: 
            return {"return_status": order["return_status"]} 
    return {"error": "Заказ с таким ID не найден"}

# Функция для создания нового заказа 
@tool 
def create_order(customer_name: str) -> Dict: 
    """ 
    Создает новый заказ. 
 
    Args: 
        customer_name (str): Имя клиента. 
 
    Returns: 
        Dict: Словарь с информацией о новом заказе. 
    """ 
    print("\033[92m" + f"Bot requested create_order({customer_name})" + "\033[0m") 
    new_order = { 
        "order_id": str(len(orders_database) + 1), 
        "customer_name": customer_name, 
        "status": "Обработка", 
        "delivery_status": "Ожидает отправки", 
        "return_status": "Нет возврата" 
    } 
    orders_database.append(new_order) 
    return new_order 

# Функция для обновления статуса заказа 
@tool 
def update_order_status(order_id: str, new_status: str) -> Dict: 
    """ 
    Обновляет статус заказа. 
 
    Args: 
        order_id (str): ID заказа. 
        new_status (str): Новый статус заказа. 
 
    Returns:
Dict: Словарь с информацией о заказе. 
    """ 
    print("\033[92m" + f"Bot requested update_order_status({order_id}, {new_status})" + 
"\033[0m") 
    for order in orders_database: 
        if order["order_id"] == order_id: 
            order["status"] = new_status 
            return order 
    return {"error": "Заказ с таким ID не найден"} 

# Функция для обновления статуса доставки 
@tool 
def update_delivery_status(order_id: str, new_delivery_status: str) -> Dict: 
    """ 
    Обновляет статус доставки заказа. 
 
    Args: 
        order_id (str): ID заказа. 
        new_delivery_status (str): Новый статус доставки. 
 
    Returns: 
        Dict: Словарь с информацией о заказе. 
    """ 
    print("\033[92m" + f"Bot requested update_delivery_status({order_id}, {new_delivery_status})" 
+ "\033[0m") 
    for order in orders_database: 
        if order["order_id"] == order_id: 
            order["delivery_status"] = new_delivery_status 
            return order 
    return {"error": "Заказ с таким ID не найден"} 

# Функция для обновления статуса возврата 
    @tool 
def update_return_status(order_id: str, new_return_status: str) -> Dict: 
    """ 
    Обновляет статус возврата заказа. 
 
    Args: 
        order_id (str): ID заказа. 
        new_return_status (str): Новый статус возврата. 
 
    Returns: 
        Dict: Словарь с информацией о заказе. 
    """ 
    print("\033[92m" + f"Bot requested update_return_status({order_id}, {new_return_status})" + 
"\033[0m") 
    for order in orders_database: 
        if order["order_id"] == order_id: 
            order["return_status"] = new_return_status 
            return order 
    return {"error": "Заказ с таким ID не найден"} 
 
system = "Ты — бот-помощник по заказам, статусам доставки и возвратам. Твоя задача — помочь пользователю с заказами, статусами доставки и возвратами." 
 
tools = [get_order_status, get_delivery_status, get_return_status, create_order, update_order_status, 
         update_delivery_status, update_return_status] 
 
giga = GigaChat( 
    credentials="!!!your_credentials!!!", 
    model="GigaChat", verify_ssl_certs=False) 
 
agent = create_react_agent(giga,                           
                           tools=tools, 
                           checkpointer=MemorySaver(), 
                           state_modifier=system_prompt) 
 
 
def chat(thread_id: str): 
    config = {"configurable": {"thread_id": thread_id}} 
    while (True): 
        rq = input("\nHuman: ") 
        print("User: ", rq) 
        if rq == "": 
            break 
        resp = agent.invoke({"messages": [("user", rq)]}, config=config) 
        print("Assistant: ", resp["messages"][-1].content) 
        time.sleep(1)  # For notebook capability 
 
 
chat(1)
