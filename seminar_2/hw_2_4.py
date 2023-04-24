# 4. Разработайте программу, которая выбросит Exception, когда пользователь вводит пустую строку.
# Пользователю должно показаться сообщение, что пустые строки вводить нельзя.
class EmptyStringException:
    pass


while True:
    try:
        user_input = input('Введите все-что угодно, кроме пустой строки :) ')
        if len(user_input) != 0:
            print(f"Отлично! У Вас всё получилось ! Вы ввели - {user_input}")
            break
        else:
            print('Пустые строки вводить нельзя ! Пробуйте еще раз. ')
    except EmptyStringException as e:
        print('Введена пустая строка! Пробуйте еще раз. ')