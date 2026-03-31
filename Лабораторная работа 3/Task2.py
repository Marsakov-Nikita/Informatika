def find_common_participants(first_group, second_group, razd=','): #Создание функции, в аргументах которой списки людей и разделитель
    first_group_list = set(first_group.split(razd)) #Первая группа (переводим список в множество для применения аргумента intersection)
    second_group_list = set(second_group.split(razd)) #Вторая группа (переводим список в множество для применения аргумента intersection)
    return sorted(list(first_group_list.intersection(second_group_list))) #Возвращаем отсортированный список общих элементов


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))