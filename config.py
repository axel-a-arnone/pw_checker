length_check = True
minimum_length = 8

lowercase_check = True

uppercase_check = True

digits_check = True

symbols_check = True
required_symbols = '~`!@#$%^&*()_-+={[}]|;<,>.?/'

std_msg = 'Password should contain at least '

length_msg = (std_msg + str(minimum_length) + ' characters')
lowercase_msg = (std_msg + 'one lowercase character')
uppercase_msg = (std_msg + 'one uppercase character')
digits_msg = (std_msg + 'one digit')
symbols_msg = (std_msg + 'one of the following symbols:\n' + required_symbols)

selected_checks = [length_check,
                   lowercase_check,
                   uppercase_check,
                   digits_check,
                   symbols_check]

msg_list = [length_msg,
            lowercase_msg,
            uppercase_msg,
            digits_msg,
            symbols_msg]

welcome_message = """Welcome to the password creator.

You will be asked to input a password that complies with some requirements.
If the selected password doesn't comply with one of the requirements, the
missing requirements will be asked again and you will have to input a new
password.
"""

success_message = "Valid password inserted! Program terminating"
