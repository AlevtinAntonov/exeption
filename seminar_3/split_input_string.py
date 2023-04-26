from datetime import datetime
from save_to_file import save_to_file

def split_input_string(input_string):
    person_name = ''
    birth_date = ''
    phone_number = ''
    male = ''
    for data in input_string:
        if data == 'm' or data == 'f':
            male = data
        elif data[2] == '.' and data[5] == '.':
            datetime.strptime(data, '%d.%m.%Y').date()
            birth_date = data
        elif data.isdigit():
            phone_number = data
        else:
            person_name += data + ' '
    print(f'FIO - {person_name}, date of birth - {birth_date}, phone - {phone_number}, male - {male} ')
    file_name = person_name.split()[0] + '.txt'
    new_string = person_name + ';' + birth_date + ';' + phone_number +';' + male
    save_to_file(file_name, new_string)

