# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file: #Открываем файл в менеджере контекста для чтения
        data_csv = csv.DictReader(file) #Десериализируем файл в виде словарей
        data_json = list(data_csv) #Составляем список словарей для сериализации в json

    with open(OUTPUT_FILENAME, 'w') as file: #Открываем файл для записи
        json.dump(data_json, file, indent=4) #Сериализуем список словарей в json, создаём файл для записи и записываем туда словари

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
