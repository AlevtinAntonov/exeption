# class DivideByZero(Exception):
#     pass
#
# def divide_num(a,b):
#     return a / b
#
# try:
#     print(divide_num(10, 0))
# except DivideByZero('jhljhhl'):
#     print('qqqqqqqqqqqqqqqqq')
# finally:
#     print('Continue ...')

class MyException(Exception):
    pass

def list_check(lst):
    if len(lst) % 2 != 0:
        raise MyException

# MyException will not be raised
list_check([1, 2, 3, 4])

# MyException will be raised
# list_check([1, 3, 5])