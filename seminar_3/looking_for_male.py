from custom_error_classes import MaleNotEnteredError


def looking_for_male(input_string):
    male_entered = False
    for data in input_string:
        if data == 'm' or data == 'f':
            male_entered = True
    if not male_entered:
        raise MaleNotEnteredError('ОШИБКА! Не введен пол в формате: f or m\n')
