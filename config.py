# CHECKS
length_check = True
lowercase_check = False
uppercase_check = False
digits_check = False
symbols_check = False

# PARAMETERS
minimum_length = 4

selected_checks = [length_check,
                   lowercase_check,
                   uppercase_check,
                   digits_check,
                   symbols_check]

welcome_message = """Welcome to the password creator.

You will be asked to input a password that complies with some requirements.
If the selected password doesn't comply with one of the requirements, the
missing requirements will be asked again and you will have to input a new
password.
"""

valid_password_message = "Valid password inserted!"


hacked_password_file_name = 'HackedPasswords.txt'
hacked_passwords_list = open(hacked_password_file_name, 'r').readlines()
hacked_passwords_list = list(map(str.strip, hacked_passwords_list))
hacked_msg = """This password appears in database of hacked passwords"""