# Задачи с LangChain и GigaChat

## Задача 1: Перевод текста

Простое приложение для перевода текста с английского на русский с использованием GigaChat.

**Файл:** [task1.py](https://github.com/kokodae/llm-tasks/blob/main/task1.py)

![Результат](https://github.com/kokodae/llm-tasks/blob/main/result1.png)

**Описание работы:**
1. Пользователь вводит текст на английском
2. Модель GigaChat переводит его на русский
3. Выводится результат перевода

**Зависимости:**
pip install langchain langchain-community gigachat

---

## Задача 2: Бот-помощник по заказам

Агент на базе GigaChat и LangGraph для работы с заказами: проверка статуса, создание заказов, обновление статусов доставки и возвратов.

**Файл:** [task2.py](https://github.com/kokodae/llm-tasks/blob/main/task2.py)

![Результат](https://github.com/kokodae/llm-tasks/blob/main/result2.png)

**Доступные инструменты (tools):**

| Инструмент | Описание |
|------------|----------|
| get_order_status | Получение статуса заказа по ID |
| get_delivery_status | Получение статуса доставки |
| get_return_status | Получение статуса возврата |
| create_order | Создание нового заказа |
| update_order_status | Обновление статуса заказа |
| update_delivery_status | Обновление статуса доставки |
| update_return_status | Обновление статуса возврата |

**Структура данных заказа:**

{
    "order_id": "1",
    "customer_name": "Иван Иванов",
    "status": "Обработка",
    "delivery_status": "Ожидает отправки",
    "return_status": "Можно вернуть"
}

---

## Установка

pip install langchain langchain-community langgraph gigachat

## Примечания

1. Для работы требуется учетная запись GigaChat и валидные credentials
2. Задача 2 использует LangGraph для управления состоянием диалога
