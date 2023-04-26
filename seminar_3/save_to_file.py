def save_to_file(file_name, new_string):
    try:
        with open(file_name, "a+", encoding="utf-8") as file:
            file.write(new_string + '\n')
        print(f'Запись добавлена в файл {file_name}')
    except IOError as e:
        print(e)



