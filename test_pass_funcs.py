# -*- coding: utf-8 -*-
import pw_check_functions as pw

# PASSWORDS
four_char_pass = 'sH0?'
eight_char_password = 'l0N?eR7!'
twelve_char_password = 'tH&L0nGesTp2'
no_lowercase = 'AL7HE0T82'
only_lowercase = 'theseareonlylowercase'
no_uppercase = 'n0?ed34r$'
only_uppercase = 'ONLYUPPERCASEPASS'
no_digits = 'noDIGts?!$'
only_digits = '42157834420'
no_symbols = 'wE0nlYDo534'
only_symbols = '+]$?)(%^@'
obvious_pw = '12345678'

# FILENAME
hacked_pw_filename = 'HackedPasswords.txt'


def test_min_length_shorter(test_pw=four_char_pass, min_length=8):
    """
    tests if a short password fails the length check

    Parameters
    ----------
    test_pw : string, optional
        Password that has to be tested. The default is four_char_pass.
    min_length : int, optional
        Minimum length that has to be checked. The default is 8.

    Returns
    -------
    None.

    """
    check = pw.min_length(test_pw, min_length)
    assert not check


def test_min_length_exact(test_pw=eight_char_password, min_lenght=8):
    """
    tests if a password of the required length passes the check

    Parameters
    ----------
    test_pw : string, optional
        Password that has to be tested. The default is eight_char_password.
    min_length : int, optional
        Minimum length that has to be checked. The default is 8.

    Returns
    -------
    None.

    """
    check = pw.min_length(test_pw, min_lenght)
    assert check


def test_min_length_longer(test_pw=twelve_char_password, min_lenght=8):
    """
    tests if password longer than requirement passes the test

    Parameters
    ----------
    test_pw : string, optional
        Password that has to be tested. The default is twelve_char_password.
    min_length : int, optional
        Minimum length that has to be checked. The default is 8.

    Returns
    -------
    None.

    """
    check = pw.min_length(test_pw, min_lenght)
    assert check


def test_lowercase_false(test_pw=no_lowercase):
    """
    tests if a password with no lowercase character fails the check

    Parameters
    ----------
    test_pw : string, optional
        Password to be checked. The default is no_lowercase.

    Returns
    -------
    None.

    """
    check = pw.lower(test_pw)
    assert not check


def test_lowercase_only_lc(test_pw=only_lowercase):
    """
    tests if a password that only contains lowercase characters passes the 
    test

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is only_lowercase.

    Returns
    -------
    None.

    """
    check = pw.lower(test_pw)
    assert check


def test_lowercase_true(test_pw=eight_char_password):
    """
    tests if a password containing lowercase characters passes the test

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is eight_char_password.

    Returns
    -------
    None.

    """
    check = pw.lower(test_pw)
    assert check


def test_uppercase_false(test_pw=no_uppercase):
    """
    tests if a password with no uppercase characters fails the test

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is no_uppercase.

    Returns
    -------
    None.

    """
    check = pw.upper(test_pw)
    assert not check


def test_uppercase_only_uc(test_pw=only_uppercase):
    """
    tests if a password with only uppercase characters passes the test

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is only_uppercase.

    Returns
    -------
    None.

    """
    check = pw.upper(test_pw)
    assert check


def test_uppercase_true(test_pw=eight_char_password):
    """
    tests if a password containing uppercase characters passes the test

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is eight_char_password.

    Returns
    -------
    None.

    """
    check = pw.upper(test_pw)
    assert check


def test_digits_false(test_pw=no_digits):
    """
    tests if a password with no digits fails the test

    Parameters
    ----------
    test_pw : string, optional
        password to be checked. The default is no_digits.

    Returns
    -------
    None.

    """
    check = pw.digits(test_pw)
    assert not check


def test_digits_only_digits(test_pw=only_digits):
    """
    tests if a password containing only digits passes the test

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is only_digits.

    Returns
    -------
    None.

    """
    check = pw.digits(test_pw)
    assert check


def test_digits_true(test_pw=eight_char_password):
    """
    tests if a password containing digits passes the test

    Parameters
    ----------
    test_pw : string, optional
        password to test. The default is eight_char_password.

    Returns
    -------
    None.

    """
    check = pw.digits(test_pw)
    assert check


def test_symbols_false(test_pw=no_symbols):
    """
    tests if a password with no symbols fails the check

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is no_symbols.

    Returns
    -------
    None.

    """
    check = pw.symbols(test_pw)
    assert not check


def test_symbols_only_symbols(test_pw=only_symbols):
    """
    tests if a password with only symbols passes the check

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is only_symbols.

    Returns
    -------
    None.

    """
    check = pw.symbols(test_pw)
    assert check


def test_symbols_true(test_pw=eight_char_password):
    """
    tests if a password containing symbols passes the check

    Parameters
    ----------
    test_pw : string, optional
        password to check. The default is eight_char_password.

    Returns
    -------
    None.

    """
    check = pw.symbols(test_pw)
    assert check


def test_pw_in_set_true(test_pw=obvious_pw, file_name=hacked_pw_filename):
    """
    tests if the password that is actually in the set is found

    Parameters
    ----------
    test_pw : string, optional
        password to look for in set. The default is obvious_pw.
    file_name : string
        Name of the txt file in which all the passwords are stored. The
        default is hacked_pw_filename.

    Returns
    -------
    None.

    """
    check = pw.check_if_in_pw_database(test_pw, file_name)
    assert check


def test_pw_in_set_false(test_pw=twelve_char_password,
                         filen_name=hacked_pw_filename):
    """
    tests if a password that isn't in the file fails the test

    Parameters
    ----------
    test_pw : string, optional
        password to test. The default is twelve_char_password.
    filen_name : string, optional
        Name of the txt file in which all the passwords are stored. The
        default is hacked_pw_filename.

    Returns
    -------
    None.

    """
    check = pw.check_if_in_pw_database(test_pw, filen_name)
    assert not check


def test_all_checks_true(test_pw='1?aBcDeFgH'):
    check = pw.all_checks(test_pw)
    assert check
