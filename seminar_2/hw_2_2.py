# 2. Если необходимо, исправьте данный код
# Задание 2
# try {
#    int d = 0;
#    double caughtRes1 = intArray[8] / d;
#    System.out.println("caughtRes1 = " + caughtRes1);
# } catch (ArithmeticException e) {
#    System.out.println("Catching exception: " + e);
# }
intArray = [1, 2, 3, 4, 5]
i = 3
d = 2
try:
    if len(intArray) <= i:
        raise IndexError(f'Индекс i = {i} за пределами массива')
    elif d == 0:
        raise ZeroDivisionError('На ноль делить нельзя!')
    elif len(intArray) > i and d != 0:
        caughtRes1 = intArray[i] / d
        print(f"caughtRes1 = {caughtRes1}")
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

