# -*- coding: utf-8 -*-

import pw_check_functions as pw
import config as cfg
import random

length_check = cfg.length_check
minimum_length = cfg.minimum_length
lowercase_check = cfg.lowercase_check
uppercase_check = cfg.uppercase_check
digits_check = cfg.digits_check
symbols_check = cfg.symbols_check


def main():
    print(cfg.welcome_message)
    print('The requirements are:')
    selected_checks_msgs = generate_requirements_list()
    for item in selected_checks_msgs:
        print(item)
    valid_password = False
    accepted_password = False
    while not accepted_password:
        while not valid_password:
            print('Would you like to generate a password randomly?')
            answer = ''
            while answer not in ('yes', 'no'):
                answer = input('Please answer yes or no: ')
                if answer == 'yes':
                    user_password = password_generator()
                    print('The generated password is:', user_password)
                elif answer == 'no':
                    user_password = input('Please input a password:\n')
                else:
                    pass
            valid_password = pw.all_checks(user_password)
        print(cfg.valid_password_message)
        pw_strength, est_guesses = pw.calculate_entropy(user_password)
        print('The password you inserted is', pw_strength)
        password_hacked = pw.hacked_password(user_password)
        if password_hacked:
            print(cfg.hacked_msg)
        print('Would you like to confirm your password?')
        answer = ''
        while answer not in ('yes', 'no'):
            answer = input('Please answer yes or no: ')
            if answer == 'yes':
                accepted_password = True
            elif answer == 'no':
                accepted_password = False
                valid_password = False
            else:
                pass
    


if __name__ == '__main__':
    main()
