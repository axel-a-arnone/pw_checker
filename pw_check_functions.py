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
    Bool
        Result of the test.

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
    Boolean
        Result of the test

    """
    lower_check = False
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
    Boolean
        Result of the test

    """
    upper_check = False
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
    Boolean
        result of the test

    """
    digits_check = False
    for char in password:
        if char.isdigit():
            digits_check = True
            break
    return digits_check


required_symbols = '~`!@#$%^&*()_-+={[}]|;<,>.?/'


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
    symbols_string = required_symbols
    symbols_dict = {}
    for symbol in enumerate(symbols_string):
        symbols_dict[symbol[0]] = symbol[1]
    # Checking for symbol in password
    symbols_check = False
    for char in password:
        if char in symbols_dict.values():
            symbols_check = True
    return symbols_check


def perform_checks(password,
                   length_check=False,
                   minimum_length=1,
                   lower_check=False,
                   upper_check=False,
                   digits_check=False,
                   symbols_check=False):
    """
    performs requested checks 

    Parameters
    ----------
    password : string
        password to test.
    length_check : Bool, optional
        Bool to perform length check. The default is False.
    minimum_length : int, optional
        Minimum length to verify. The default is 1.
    lower_check : Bool, optional
        Bool to perform lowercase check. The default is False.
    upper_check : Bool, optional
        Bool to perform uppercase check. The default is False.
    digits_check : Bool, optional
        Bool to perform digits check. The default is False.
    symbols_check : Bool, optional
        Bool to perform symbols check. The default is False.

    Returns
    -------
    check_return
        True if all tests are true, False if the password fails at least one
        test.

    """

    check_list = [True]
    if length_check:
        check_list.append(min_length(password, minimum_length))
    if lower_check:
        check_list.append(lower(password))
    if upper_check:
        check_list.append(upper(password))
    if digits_check:
        check_list.append(digits(password))
    if symbols_check:
        check_list.append(symbols(password))

    check_return = True

    for check in check_list:
        if not check:
            check_return = False
            break
    
    return check_return


std_msg = 'Password should contain at least '


def get_length_message(minimum_length):
    """
    Creates length message string given a minimum_length

    Parameters
    ----------
    minimum_length : int
        Required minimum length.

    Returns
    -------
    length_msg : str
        message stating that the password should contain the required minimum
        ammount of characters.

    """
    length_msg = (std_msg + str(minimum_length) + ' characters')
    return length_msg


lowercase_msg = (std_msg + 'one lowercase character')
uppercase_msg = (std_msg + 'one uppercase character')
digits_msg = (std_msg + 'one digit')
symbols_msg = (std_msg + 'one of the following symbols:\n' + required_symbols)


def print_missing_requirements(password,
                               length_check=False,
                               minimum_length=1,
                               lower_check=False,
                               upper_check=False,
                               digits_check=False,
                               symbols_check=False):
    """
    prints message prompting the password requirements

    Parameters
    ----------
    password : str
        password to test.
    length_check : Bool, optional
        Bool to perform length check. The default is False.
    minimum_length : int, optional
        Minimum length to verify. The default is 1.
    lower_check : Bool, optional
        Bool to perform lowercase check. The default is False.
    upper_check : Bool, optional
        Bool to perform uppercase check. The default is False.
    digits_check : Bool, optional
        Bool to perform digits check. The default is False.
    symbols_check : Bool, optional
        Bool to perform symbols check. The default is False.

    Returns
    -------
    None.

    """
    if length_check:
        if not min_length(password, minimum_length):
            length_msg = get_length_message(minimum_length)
            print(length_msg)
    if lower_check:
        if not lower(password):
            print(lowercase_msg)
    if upper_check:
        if not upper(password):
            print(uppercase_msg)
    if digits_check:
        if not digits(password):
            print(digits_msg)
    if symbols_check:
        if not symbols(password):
            print(symbols_msg)


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


def check_if_in_pw_database(password, password_database_file_name):
    password_database_file = open(password_database_file_name, 'r').readlines()
    password_database_set = set(map(str.strip, password_database_file))
    pw_in_set = False
    if password in password_database_set:
        pw_in_set = True
    return pw_in_set
