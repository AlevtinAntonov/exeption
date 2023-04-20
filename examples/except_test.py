try:
    print(10 / '0')
# except ZeroDivisionError as e:
#     print(isinstance(e, ZeroDivisionError))
#     print(isinstance(e, str))
#     print(isinstance(e, Exception))
#     print(e, object)
#     print(e)
# except TypeError as e:
#     print(e)
except Exception as e:
    print(e)
# except:
#     print('Some error occurred')

else:
    print('There was no error')
finally:
    print('Continue ...')

def divide_num(a,b):
    if b == 0:
        raise ValueError("Second arg can not be Zero")
    return a / b

try:
    divide_num(10, 0)
except Exception as e:
    print(e)
finally:
    print('Continue ...')
