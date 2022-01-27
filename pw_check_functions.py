# -*- coding: utf-8 -*-


def min_length(password):
    min_length = 8
    min_length_error = 'The password is too short'
    if len(password) >= min_length:
        return True
    else:
        return min_length_error


def lower(password):
    lower_check = 'The password does not have any lowercase character'
    for char in password:
        if char.islower():
            lower_check = True
            break
    return lower_check


def upper(password):
    upper_check = 'The password does not have any uppercase character'
    for char in password:
        if char.isupper():
            upper_check = True
            break
    return upper_check


def digits(password):
    digits_check = 'The password does not have any digits'
    for char in password:
        if char.isdigit():
            digits_check = True
            break
    return digits_check


def symbols(password):
    # Setting symbols string and dict
    symbols_string = '~`!@#$%^&*()_-+={[}]|;<,>.?/'
    symbols_dict = {}
    for symbol in enumerate(symbols_string):
        symbols_dict[symbol[0]] = symbol[1]
    # Checking for symbol in password
    symbols_check = 'The password does not have any of the selected symbols'
    for char in password:
        if char in symbols_dict.values():
            symbols_check = True
    return symbols_check


def all_checks(password):
    check_return = True
    check_list = [min_length(password),
                  lower(password),
                  upper(password),
                  digits(password),
                  symbols(password)]
    for check in check_list:
        if check is not True:
            check_return = False
            print(check)
    return check_return
