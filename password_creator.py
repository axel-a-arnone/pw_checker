# -*- coding: utf-8 -*-

import pw_check_functions as pw
import config as cfg


def generate_requirements_list():
    """
    Generates the list of requirements from config file

    Returns
    -------
    selected_checks_msgs : List of strings
        Each element is a password requirement.

    """
    selected_checks_msgs = cfg.msg_list
    for idx, check in enumerate(cfg.selected_checks):
        if not check:
            _ = selected_checks_msgs.pop(idx)
    return selected_checks_msgs


def main():
    print(cfg.welcome_message)
    print('The requirements are:')
    selected_checks_msgs = generate_requirements_list()
    for item in selected_checks_msgs:
        print(item)
    valid_password = False
    while not valid_password:
        user_password = input('Please input a password:\n')
        valid_password = pw.all_checks(user_password)
    print(cfg.success_message)


if __name__ == '__main__':
    main()
