from custom_error_classes import PhoneNumberInputError


def looking_for_phone(input_string):
    check_for_phone = False
    for data in input_string:
        if data.isdigit():
            check_for_phone = True
    if not check_for_phone:
        raise PhoneNumberInputError('ОШИБКА ! Не введен номер телефона\n')
