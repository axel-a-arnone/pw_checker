# Password checker
## _A tester for your passwords_

![GitHub language count](https://img.shields.io/github/languages/count/axel-a-arnone/pw_checker)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/axel-a-arnone/pw_checker)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/axel-a-arnone/pw_checker)

Password Checker is a program that guides you through a password creation process, and allows you to select the password requirements.

## Features

- Checking the strength of the selected password
- Estimating the number of tries necessary to guess it
- Checking if the input password appears in a hacked passwords database
- Automatically generate a compliant password


## Installation

Download the full repository and save it in a folder.

---

## Usage and configuration

To try the program, run password_creator.py
You will be prompted with the password requirements and the possibility to automatically generate a password
At the end of the process, the program will check if the password is in the provided hacked passwords database

The password password requirements can be tweaked in the config file:

<img src="https://github.com/axel-a-arnone/pw_checker/blob/main/images/config_img.png" width="400">

Currently, the only password requirement is to have at least 4 characters.
Changing the booleans in the CHECKS section of the config file will turn on checks for other conditions, such as presence of lowercase letters, uppercase letters, digits and special symbols.
If you would like to use a different password database, add another txt file with one password per row and change the pass_db_filename value.

---

## Development

Want to contribute? Great!

This program started as a project for my programming course, but I'd be happy to expand it.
If you have any suggestions on how to improve the code, or what features I could add, please contact me!


## License

**Free Software, Hell Yeah!**

