import random
import datetime


def remove_repeat_characters(message):
    message = ''.join(
        [char for index, char in enumerate(message) if char not in message[0:index]])
    return message


def input_checker(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input
            break


def write_passwords():
    chars = str('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()+|}{":?><,./;[]')
    password = ''
    passwordArray = []
    name = str(input("What is your name?"))
    numOfPasswords = input_checker("How many passwords would you like to generate?")
    passwordConstructCounter = 1
    numOfPasswordCounter = 1
    pass_write = open("passwords.txt", "a+")
    for p in range(numOfPasswords):
        passwordLength = input_checker("How long would you like password " + str(numOfPasswordCounter) + " to be?")
        numOfPasswordCounter += 1
        removedCharacters = str(input("Which characters are disallowed?"))
        while chars.translate(str.maketrans('', '', removedCharacters)) == '':
            print("You may not disallow all characters. Please try again.")
            removedCharacters = str(input("Which characters are disallowed?"))
        chars = chars.translate(str.maketrans('', '', removedCharacters))
        for c in range(int(passwordLength)):
            password += random.choice(chars)
        passwordArray.append(password)
        chars = str('abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()+|}{":?><,./;[]')
        password = ''
    pass_write.write("\nThese are the passwords for " + name + " on " + str(datetime.datetime.now()) + "\n")
    print("Here are your passwords:")
    for x in passwordArray:
        pass_write.write(str(passwordConstructCounter) + ". " + x + "\n")
        print(str(passwordConstructCounter) + ". " + x)
        passwordConstructCounter += 1
    pass_write.close()
    input("Press Enter to continue")


def read_passwords():
    try:
        stored_pass = open("passwords.txt", "r+")
    except FileNotFoundError:
        print("No passwords.txt file was found.")
        main()
    passwords = stored_pass.read()
    print(passwords)
    stored_pass.close()
    input("Press Enter to continue")

def main():
    readOrWrite = str(input("Would you like to read or write passwords?"))
    while readOrWrite != 'read' and readOrWrite != 'write':
        readOrWrite = str(input("Please enter either \"read\" or \"write\""))
    if readOrWrite == 'read':
        read_passwords()
    else:
        write_passwords()


print("Hello! Welcome to PyPass.")
main()
