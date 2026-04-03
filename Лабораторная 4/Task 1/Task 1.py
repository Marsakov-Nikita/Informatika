# TODO решите задачу
import json

def task() -> float: #Создание функции
    with open('input.json', 'r') as file: #Открытие файла в менеджере контекста
        data = json.load(file) #Десериализация файла json
        summ = 0 #Переменная для накопления суммы произведений
        for i in data: #Проход по всем словарям
            summ += i['score'] * i['weight'] #Суммирование произведений по ключам
    return round(summ, 3) #Возвращение округлённого значения


print(task())
