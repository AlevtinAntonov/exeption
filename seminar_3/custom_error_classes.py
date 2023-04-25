class CustomError(Exception):
    pass


class NumberOfInputDataWrongError(CustomError):
    """Количество введенных данных не совпадает с требуемым"""


class MaleNotEnteredError(CustomError):
    """Не введен пол в формате: f or m"""


class DateInputError(CustomError):
    """Не введена дата рождения в формате dd.mm.yyyy"""
