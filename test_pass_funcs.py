# -*- coding: utf-8 -*-
import pw_check_functions as pw


four_char_pass = 'sH0?'
eight_char_password = 'l0N?eR7!'
twelve_char_password = 'tH&L0nGesTp2'


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


def test_lowercase_false(test_pw='ALLCAPS'):
    check = pw.lower(test_pw)
    assert isinstance(check, str)


def test_lowercase_true(test_pw='CAPSandlower'):
    check = pw.lower(test_pw)
    assert check


def test_uppercase_false(test_pw='nocaps'):
    check = pw.upper(test_pw)
    assert isinstance(check, str)


def test_uppercase_true(test_pw='CAPSandlower'):
    check = pw.upper(test_pw)
    assert check


def test_digits_fales(test_pw='NoDiGiTs'):
    check = pw.digits(test_pw)
    assert isinstance(check, str)


def test_digits_true(test_pw='alsodigits123'):
    check = pw.digits(test_pw)
    assert check


def test_symbols_false(test_pw='nosymbols'):
    check = pw.symbols(test_pw)
    assert isinstance(check, str)


def test_symbols_true(test_pw='alsosymbols?'):
    check = pw.symbols(test_pw)
    assert check


def test_all_checks_true(test_pw='1?aBcDeFgH'):
    check = pw.all_checks(test_pw)
    assert check
