# -*- coding: utf-8 -*-
import config as cfg


def min_length(password):
    """
    Checks if password has minimum length, defined in config file

    Parameters
    ----------
    password : String
        Password to test.

    Returns
    -------
    True or Error string
        True if: password is long enough, else: error string.

    """
    min_length = cfg.minimum_length
    min_length_msg = cfg.length_msg
    if len(password) >= min_length:
        return True
    else:
        return min_length_msg


def lower(password):
    """
    Checks if password has at least one lowercase character

    Parameters
    ----------
    password : String
        Password to test.

    Returns
    -------
    True or Error string
        True if: password has at least one lowercase character,
        else: error string.

    """
    lower_check = cfg.lowercase_msg
    for char in password:
        if char.islower():
            lower_check = True
            break
    return lower_check


def upper(password):
    """
    Checks if password has at least one uppercase character

    Parameters
    ----------
    password : String
        Password to test.

    Returns
    -------
    True or Error string
        True if: password has at least one uppercase character,
        else: error string.

    """
    upper_check = cfg.uppercase_msg
    for char in password:
        if char.isupper():
            upper_check = True
            break
    return upper_check


def digits(password):
    """
    Checks if password has at least one digit

    Parameters
    ----------
    password : String
        Password to test.

    Returns
    -------
    True or Error string
        True if: password has at least one digit, else: error string.

    """
    digits_check = cfg.digits_msg
    for char in password:
        if char.isdigit():
            digits_check = True
            break
    return digits_check


def symbols(password):
    """
    Checks if password has at least one special symbol, defined in config file

    Parameters
    ----------
    password : String
        Password to test.

    Returns
    -------
    True or Error string
        True if: password has at least one special symbol, else: error string.

    """
    # Setting symbols string and dict
    symbols_string = cfg.required_symbols
    symbols_dict = {}
    for symbol in enumerate(symbols_string):
        symbols_dict[symbol[0]] = symbol[1]
    # Checking for symbol in password
    symbols_check = cfg.symbols_msg
    for char in password:
        if char in symbols_dict.values():
            symbols_check = True
    return symbols_check


def all_checks(password):
    """
    Performs selected password checks

    Parameters
    ----------
    password : String
        Password to test.

    Returns
    -------
    check_return : Bool
        If password fails a test, function will print related requirement

    """
    check_return = True
    check_list = [min_length(password),
                  lower(password),
                  upper(password),
                  digits(password),
                  symbols(password)]
    # Removing unwanted checks
    selected_checks = cfg.selected_checks
    for idx, check in enumerate(selected_checks):
        if not check:
            _ = check_list.pop(idx)
    # Reading check results
    for check in check_list:
        if check is not True:
            check_return = False
            print(check)
    return check_return
