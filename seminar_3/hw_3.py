# Напишите приложение, которое будет запрашивать у пользователя следующие данные
# в произвольном порядке, разделенные пробелом:
# Фамилия Имя Отчество датарождения номертелефона пол
# Форматы данных:
# фамилия, имя, отчество - строки
# дата_рождения - строка формата dd.mm.yyyy
# номер_телефона - целое беззнаковое число без форматирования
# пол - символ латиницей f или m.
# Приложение должно проверить введенные данные по количеству. Если количество не совпадает с требуемым,
# вернуть код ошибки, обработать его и показать пользователю сообщение, что он ввел меньше и больше данных,
# чем требуется.
# Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры.
# Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы.
# Можно использовать встроенные типы java и создать свои. Исключение должно быть корректно обработано,
# пользователю выведено сообщение с информацией, что именно неверно.
# Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии, в него в одну
# строку должны записаться полученные данные, вида
# <Фамилия><Имя><Отчество><датарождения> <номертелефона><пол>
# Однофамильцы должны записаться в один и тот же файл, в отдельные строки.
# Не забудьте закрыть соединение с файлом.
# При возникновении проблемы с чтением-записью в файл, исключение должно быть корректно обработано,
# пользователь должен увидеть стектрейс ошибки.
# 19.03.1964 89217730009 Antonov Alevtin Ivanovich m
class CustomError(Exception):
    pass


class NumberOfInputDataWrongError(CustomError):
    """Количество введенных данных не совпадает с требуемым"""

class MaleNotEnteredError(CustomError):
    """Не введен пол в формате: f or m"""

class DateInputError(CustomError):
    """Не введена дата рождения в формате dd.mm.yyyy"""


def split_input_string(input_string):

    person_name = ''
    birth_date = ''
    phone_number = ''
    male = ''
    for data in input_string:
        if data == 'm' or data == 'f':
            male = data
        elif data[2] == '.' and data[5] == '.':

            # if data[0].isdigit() and
            birth_date = data
        elif data.isdigit():
            phone_number = data
        else:
            person_name = person_name + ' ' + data
    print(f'FIO - {person_name}, date of birth - {birth_date}, phone - {phone_number}, male - {male} ')
    return person_name, male, birth_date, phone_number

while True:

    input_string = input('Введите следующие данные в произвольном порядке, разделенные пробелом:\n'
                         'фамилия имя отчество - не меняя порядок ФИО\n'
                         'дата_рождения - строка формата dd.mm.yyyy\n'
                         'номер_телефона - целое беззнаковое число без форматирования\n'
                         'пол - символ латиницей f или m : \n').split()

    # print(input_string)
    try:
        male_entered = False
        date_of_birth_check = False
        if len(input_string) < 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> меньше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif len(input_string) > 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> больше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif not male_entered:
            for data in input_string:
                if data == 'm' or data == 'f':
                    male_entered = True
            if male_entered:
                pass
            else:
                raise MaleNotEnteredError('ОШИБКА ! Не введен пол.')

        elif not date_of_birth_check:
            for data in input_string:
                print(data)
                if len(data) == 10 and data[2] == '.' and data[5] == '.':
                    date_of_birth_check = True
                    print(data, len(data), data[2], data[5], 'date ok')
            if date_of_birth_check:

                pass
            else:
                print('hgghghghhg')
                raise DateInputError('Ошибка! не введена дата рождения в формате dd.mm.yyyy')

    except NumberOfInputDataWrongError as e:
        print(e)
    except MaleNotEnteredError as e:
        print(e)
    except DateInputError as e:
        print(e)
    else:
        split_input_string(input_string)
        break





        # for data in input_string:
        #     if len(data) == 10 and data[2] == '.' and data[5] == '.':
        #         print(data, len(data), data[2], data[5], 'date ok')
        #     else:
        #         raise DateInputError('Ошибка! не введена дата рождения в формате dd.mm.yyyy')





