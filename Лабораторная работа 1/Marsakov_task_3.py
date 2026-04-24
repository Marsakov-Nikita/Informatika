players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]


middle_index = len(players) // 2 # Индекс середины

first_com = players[:middle_index] # Первая команда
second_com = players[middle_index:] # Вторая команда

# Вывод команд
print(first_com)
print(second_com)
