# -*- coding: utf-8 -*-

import pw_check_functions as pw
import config as cfg

welcome_message = """Welcome to the password generator.
Your task is to input a password that complies with the following:
    - Min 8 characters long
    - Min one lowercase letter
    - Min one uppercase letter
    - Min one digit
    - Min one of the following symbols:
            ~`!@#$%^&*()_-+={[}]|;<,>.?/

    You will be asked to input a new password until you insert a valid one!"""

password_requirements = """Password requirements:
    - Min 8 characters long
    - Min one lowercase letter
    - Min one uppercase letter
    - Min one digit
    - Min one of the following symbols:
            ~`!@#$%^&*()_-+={[}]|;<,>.?/"""

success_message = "Valid password inserted! Program terminating"


def generate_requirements_list():
    seleceted_checks_msgs = cfg.msg_list
    for idx, check in enumerate(cfg.selected_checks):
        if not check:
            _ = seleceted_checks_msgs.pop(idx)
    return seleceted_checks_msgs

def main():
    print(welcome_message)
    valid_password = False
    while not valid_password:
        user_password = input('Please input a password:\n')
        valid_password = pw.all_checks(user_password)
    print(success_message)


if __name__ == '__main__':
    main()
