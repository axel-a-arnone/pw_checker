# -*- coding: utf-8 -*-
import pw_check_functions as pw


def test_min_length_false(test_pw='short'):
    check = pw.min_length(test_pw)
    assert isinstance(check, str)


def test_min_length_true(test_pw='longerpassword'):
    check = pw.min_length(test_pw)
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
