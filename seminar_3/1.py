data = '01.01.1956'

if len(data) == 10 and data[2] == '.' and data[5] == '.':
    print(data, len(data), data[2], data[5], 'date ok')
elif data[0].isdigit() and data[1].isdigit():
    print('ddddd')
