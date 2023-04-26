class CustomError(Exception):
    pass


class NumberOfInputDataWrongError(CustomError):
    """Количество введенных данных не совпадает с требуемым"""
    pass


class MaleNotEnteredError(CustomError):
    """Не введен пол в формате: f or m"""
    pass


class DateInputError(CustomError):
    """Не введена дата рождения в формате dd.mm.yyyy"""
    pass


class PhoneNumberInputError(CustomError):
    """Не введен номер телефона """
    pass
