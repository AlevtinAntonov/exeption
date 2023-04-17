# Реализуйте метод, принимающий в качестве аргумента целочисленный массив и некоторое значение. Метод ищет в массиве заданное значение и возвращает его индекс. При этом, например:
# если длина массива меньше некоторого заданного минимума, метод возвращает -1, в качестве кода ошибки.
# если искомый элемент не найден, метод вернет -2 в качестве кода ошибки.
# если вместо массива пришел null, метод вернет -3
# придумайте свои варианты исключительных ситуаций и верните соответствующие коды ошибок.
# Напишите метод, в котором реализуйте взаимодействие с пользователем. То есть, этот метод запросит искомое число у пользователя, вызовет первый, обработает возвращенное значение и покажет читаемый результат пользователю. Например, если вернулся -2, пользователю выведется сообщение: “Искомый элемент не найден”.


MIN_ARRAY_LENGTH = 3


def get_ind(arr, val):
    if arr:
        if len(arr) < MIN_ARRAY_LENGTH:
            return -1
        elif val in arr:
            return arr.index(val)
        else:
            return -2
    return -3


array = [1, 2, 3, 4, 5]
value = int(input("Введите число для поиска в массиве: "))
result = get_ind(array, value)
match result:
    case -1:
        print("Длина массива меньше минимума")
    case -2:
        print("Искомый элемент не найден")
    case -3:
        print("Пустой массив")
    case _:
        print(f"Индекс элемента: {result}")

