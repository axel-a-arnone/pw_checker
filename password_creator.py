# -*- coding: utf-8 -*-

import pw_check_functions as pw
import config as cfg
import random


def generate_requirements_list():
    """
    Generates the list of requirements from config file

    Returns
    -------
    selected_checks_msgs : List of strings
        Each element is a password requirement.

    """
    checks_msgs_base = cfg.msg_list
    selected_checks_msgs = []
    for idx, check in enumerate(cfg.selected_checks):
        if check:
            selected_checks_msgs.append(checks_msgs_base[idx])
    return selected_checks_msgs


def password_generator():
    """
    Generates password based on the settings of the configuration files

    Returns
    -------
    gen_password : string
        Random generated password, with at least one element from each
        character type.

    """
    pass_length = 12
    if cfg.length_check:
        min_len = cfg.minimum_length
        pass_length = min_len + random.randint(0, min_len)
    gen_lists = cfg.all_chartypes
    number_of_types = len(gen_lists)
    gen_password = ''
    for idx in range(number_of_types):
        gen_char = random.choice(gen_lists[idx])
        gen_password += gen_char
    for idx in range(pass_length-number_of_types):
        gen_char = random.choice(random.choice(gen_lists))
        gen_password += gen_char
    return gen_password


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
            user_password = input('Please input a password:\n')
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
