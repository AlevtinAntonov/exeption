from custom_error_classes import DateInputError


def looking_for_date(input_string):
    check_for_date = False
    for data in input_string:
        if len(data) == 10 and data[2] == '.' and data[5] == '.':
            str_replace = data.replace('.', '')
            if str_replace.isdigit():
                check_for_date = True
    if not check_for_date:
        raise DateInputError('ОШИБКА! Не введена дата рождения в формате dd.mm.yyyy\n')
