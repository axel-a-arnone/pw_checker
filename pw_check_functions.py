# -*- coding: utf-8 -*-
def min_length(password):
    min_length = 8
    if len(password) >= min_length:
        return True
    else:
        return False


def lower(password):
    lower_check = False
    for char in password:
        if char.islower():
            lower_check = True
            break
    return lower_check


def upper(password):
    upper_check = False
    for char in password:
        if char.isupper():
            upper_check = True
            break
    return upper_check


def digits(password):
    digits_check = False
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
    symbols_check = False
    for char in password:
        if char in symbols_dict.values():
            symbols_check = True
    return symbols_check


def all_checks(password):
    if not min_length(password):
        return False
    if not lower(password):
        return False
    if not upper(password):
        return False
    if not digits(password):
        return False
    if not symbols(password):
        return False
    return True
