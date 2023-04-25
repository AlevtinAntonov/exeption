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
# 19,03.1964 89217730009 Antonov Alevtin Ivanovich m

from custom_error_classes import *
from split_input_string import split_input_string
from looking_for_date import looking_for_date
from looking_for_male import looking_for_male

male_entered = ''
check_for_date = ''

while True:

    input_string = input('Введите следующие данные в произвольном порядке, разделенные пробелом:\n'
                         'фамилия имя отчество - не меняя порядок ФИО\n'
                         'дата_рождения - строка формата dd.mm.yyyy\n'
                         'номер_телефона - целое беззнаковое число без форматирования\n'
                         'пол - символ латиницей f или m : \n').split()

    # print(input_string)

    try:
        looking_for_male(input_string)
        print(male_entered)
        looking_for_date(input_string)
        print(check_for_date)

        if len(input_string) < 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> меньше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif len(input_string) > 6:
            raise NumberOfInputDataWrongError(f'ОШИБКА! Количество данных = {len(input_string)} -> больше требуемых 6\n'
                                              'Попробуйте ввести ещё раз\n')
        elif not male_entered:
            raise MaleNotEnteredError('ОШИБКА ! Не введен пол.\n')
        elif not check_for_date:
            raise DateInputError('Не введена дата рождения в формате dd.mm.yyyy\n')


    except NumberOfInputDataWrongError as e:
        print(e)
    except MaleNotEnteredError as e:
        print(e)
    except DateInputError as e:
        print(e)
    else:
        split_input_string(input_string)
        break

        if male_entered:
            print('date_of_birth_check = ', date_of_birth_check)
        elif date_of_birth_check is False:
            print('date_of_birth_check = ', date_of_birth_check)
            for data in input_string:
                print(data)
                if len(data) == 10 and data[2] == '.' and data[5] == '.':
                    date_of_birth_check = True
                    print(data, len(data), data[2], data[5], 'date ok')
            if date_of_birth_check:
                pass
            else:
                print('hgghghghhg')
                raise DateInputError('Ошибка! не введена дата рождения в формате dd.mm.yyyy\n')
