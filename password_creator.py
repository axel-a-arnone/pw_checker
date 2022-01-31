# -*- coding: utf-8 -*-

import pw_check_functions as pw
import config as cfg

length_check = cfg.length_check
minimum_length = cfg.minimum_length
lowercase_check = cfg.lowercase_check
uppercase_check = cfg.uppercase_check
digits_check = cfg.digits_check
symbols_check = cfg.symbols_check

hacked_pw_database = cfg.pass_db_filename

welcome_message = """Welcome to the password creator.

You will be asked to input a password that complies with some requirements.
If the selected password doesn't comply with one of the requirements, the
missing requirements will be asked again and you will have to input a new
password.
"""

valid_password_message = "Valid password inserted!"

hacked_msg = """This password appears in database of HACKED passwords"""


def main():
    print(welcome_message)
    print('The requirements are:')
    user_password = ''
    valid_password = False
    accepted_password = False
    while not accepted_password:
        while not valid_password:
            pw.print_missing_requirements(user_password,
                                          length_check,
                                          minimum_length,
                                          lowercase_check,
                                          uppercase_check,
                                          digits_check,
                                          symbols_check)
            print('Would you like to generate a password randomly?')
            answer = ''
            while answer not in ('yes', 'no'):
                answer = input('Please answer yes or no: ')
                if answer == 'yes':
                    user_password = pw.password_generator(length_check,
                                                          minimum_length)
                    print('The generated password is:', user_password)
                elif answer == 'no':
                    user_password = input('Please input a password:\n')
                else:
                    pass
            valid_password = pw.perform_checks(user_password,
                                               length_check,
                                               minimum_length,
                                               lowercase_check,
                                               uppercase_check,
                                               digits_check,
                                               symbols_check)
        print(valid_password_message)
        pw_strength, est_guesses = pw.calculate_entropy(user_password)
        print('The password you inserted is', pw_strength)
        password_hacked = pw.check_if_in_pw_database(user_password,
                                                     hacked_pw_database)
        if password_hacked:
            print(hacked_msg)
        print('Would you like to confirm your password?')
        answer = ''
        while answer not in ('yes', 'no'):
            answer = input('Please answer yes or no: ')
            if answer == 'yes':
                accepted_password = True
            elif answer == 'no':
                accepted_password = False
                valid_password = False
                user_password = ''
            else:
                pass


if __name__ == '__main__':
    main()
