# -*- coding: utf-8 -*-
import config as cfg
import math


def min_length(password, minimum_length):
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
    if len(password) >= minimum_length:
        return True
    else:
        return False


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
    check_list_base = [min_length(password),
                       lower(password),
                       upper(password),
                       digits(password),
                       symbols(password)]
    check_list = []
    # Removing unwanted checks
    selected_checks = cfg.selected_checks
    for idx, check in enumerate(selected_checks):
        if check:
            check_list.append(check_list_base[idx])
    # Reading check results
    for check in check_list:
        if check is not True:
            check_return = False
            print(check)
    return check_return


def calculate_entropy(password):
    """
    Evaluates strength of inserted password

    Parameters
    ----------
    password : string
        Password to be tested.

    Returns
    -------
    pw_strength : String
        Strength of password based on entropy.
    expected_number_of_guesses : Int
        Estimated number of guesses.

    """
    password_length = len(password)
    char_lists = cfg.all_chartypes
    char_counters = []
    for _ in char_lists:
        char_counters.append(0)
    for char in password:
        for idx, cur_list in enumerate(char_lists):
            if char in cur_list:
                char_counters[idx] += 1
                break
    possible_characters = 0
    for idx, counter in enumerate(char_counters):
        if counter != 0:
            possible_characters += len(char_lists[idx])
    possible_combinations = possible_characters ** password_length
    pw_entropy = math.log(possible_combinations, 2)
    expected_number_of_guesses = 2 ** round(pw_entropy-1)
    entropy_levels = [28, 35, 59, 127, 256]
    pw_strength_levels = ['Very weak...',
                          'Weak',
                          'Reasonable',
                          'Strong',
                          'Insanely strong!']
    for idx, limit in enumerate(entropy_levels):
        if pw_entropy < limit:
            pw_strength = pw_strength_levels[idx]
            break
    return pw_strength, expected_number_of_guesses


def hacked_password(password):
    """
    Verifies if password is in database of hacked passwords

    Parameters
    ----------
    password : string
        password being tested.

    Returns
    -------
    hacked: Bool
        Boolean stating if selected password has already been hacked or not

    """
    hacked = False
    if password in cfg.hacked_passwords_list:
        hacked = True
    return hacked
