# CHECKS
length_check = True
lowercase_check = False
uppercase_check = False
digits_check = False
symbols_check = False

# PARAMETERS
minimum_length = 4


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

valid_password_message = "Valid password inserted!"

all_lowercase = ['a', 'b', 'c', 'd', 'e',
                 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']

all_uppercase = ['A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

all_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

all_symbols = []

for symbol in required_symbols:
    all_symbols.append(symbol)

all_chartypes = [all_lowercase,
                 all_uppercase,
                 all_digits,
                 all_symbols]


hacked_password_file_name = 'HackedPasswords.txt'
hacked_passwords_list = open(hacked_password_file_name, 'r').readlines()
hacked_passwords_list = list(map(str.strip, hacked_passwords_list))
hacked_msg = """This password appears in database of hacked passwords"""