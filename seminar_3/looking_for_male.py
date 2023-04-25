def looking_for_male(input_string):
    male_entered = False
    for data in input_string:
        if data == 'm' or data == 'f':
            male_entered = True
    return male_entered
