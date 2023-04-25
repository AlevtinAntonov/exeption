def looking_for_date(test_list):
    check_for_date = False
    for data in test_list:
        if len(data) == 10 and data[2] == '.' and data[5] == '.':
            check_for_date = True
    return check_for_date
