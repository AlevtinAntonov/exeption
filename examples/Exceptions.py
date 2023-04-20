# #Intuition to Try Except
# a=0
# b=2
#
# c = b/a
# c= b*b
# print(c)
#
# # Exception types
# a = 0
# b = 2
# try:
#     c = b / a
#
# except ZeroDivisionError:
#     a = 1
#
#     print("This is not possible")
#     c = b / a
#
# print(c)
#
# #Except Name Error
# a=10
# b=2
# i=3
# try:
#     c=a/x
# except NameError:
#     c=a/i
#     print("Variable is not yet created")
#
# print(c)
#
# #Except Else
# a=10
# b=2
# i=3
# x=5
# try:
#     c=a/x
# except NameError:
#     c=a/i
#     print("Variable is not yet created")
# else:
#     x=100
#     print(x)
#
# # Except Else Finally
# a = 10
# b = 2
# i = 3
#
# try:
#     c = a / x
# except NameError:
#     c = a / i
#     print("Variable is not yet created")
# else:
#     x = 100
#     print(x)
#
# finally:
#     print("I will be executed no matter what!")
#
# # Mock example
# # i wanna create a folder that contains 5 files
# # There is a chance that this folder is already created by a previoous program run
#
# try:
#     print("I am trying to create a folder")
#
# except:
#     print("folder does exist! cannot be created")
#
# else:
#     print("Put 5 files in that folder!")
#
#
# finally:
#     print("Folder created successfuly!")
#
# a = 0
# b = 2
# try:
#     c = b / x
#
# except Exception as e:
#     print(e)
#
# import sys
# a="0"
# b=5
#
# try:
#     c=b/a
# except NameError:
#     print("Variable Does not Exist!")
#     print("Creating Variable")
#     a=1
#     c=b/a
# except ZeroDivisionError:
#     print("Cannot be divided by zero.")
#     print("Adjusting Value..")
#     a=1
#     c=b/a
# except Exception as e:
#     print(e)
#     print("Sorry but an error occured. Exiting")
#
# else:
#     print(c)


class CustomEx(Exception):
    """Class Customs Exceptions"""


class ElementDoesNotExist(CustomEx):
    pass


class FirstElementIsSmallerThanSecond(Exception):
    """firstElementIsSmallerThanSecond"""


l = [1, 2, 3, 4, 5]

# if not 3 in l:
#     raise ElementDoesNotExist
# elif l[0] < l[1]:
#     raise FirstElementIsSmallerThanSecond("Class Customs Exceptions")

try:
    if not 3 in l:
        raise ElementDoesNotExist
    elif l[0] < l[1]:
        raise FirstElementIsSmallerThanSecond

except ElementDoesNotExist:
    print("Element Does not Exist. Raising an Exception")

except FirstElementIsSmallerThanSecond:
    print("1st element is smaller. Raising an exception")
else:
    print("Success element exist!")
