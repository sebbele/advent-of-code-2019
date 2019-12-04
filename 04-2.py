#!/usr/bin/env python

input = [307237, 769058]

def validatePassword(password, input):
    pass_string = str(password)
    # check if length = 6 digits
#    if not len(pass_string) == 6:
#        return False
    # find adjacent digits pair
    pair_found = False
    if pass_string[0] == pass_string[1] and pass_string[2] != pass_string[0]:
        pair_found = True
    elif pass_string[1] == pass_string[2] and pass_string[0] != pass_string[1] and pass_string[3] != pass_string[1]:
        pair_found = True
    elif pass_string[2] == pass_string[3] and pass_string[1] != pass_string[2] and pass_string[4] != pass_string[2]:
        pair_found = True
    elif pass_string[3] == pass_string[4] and pass_string[2] != pass_string[3] and pass_string[5] != pass_string[3]:
        pair_found = True
    elif pass_string[4] == pass_string[5] and pass_string[3] != pass_string[4]:
        pair_found = True
    if not pair_found:
        return False
    # check if numbers never decrease
    if int(pass_string[0]) > int(pass_string[1]):
        return False
    elif int(pass_string[1]) > int(pass_string[2]):
        return False
    elif int(pass_string[2]) > int(pass_string[3]):
        return False
    elif int(pass_string[3]) > int(pass_string[4]):
        return False
    elif int(pass_string[4]) > int(pass_string[5]):
        return False

    return True

if __name__ == "__main__":
    result = []
    for i in range(input[0], input[1] + 1):
        if validatePassword(i, input):
            result.append(i)
    print(result)
    print(len(result))
