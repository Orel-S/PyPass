import random
import msvcrt as visualc


def wait_for_input():
    visualc.getch()


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


chars = str('abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()+|}{":?><,./;[]')
password = ''
passwordArray = []
numOfPasswords = input_checker("How many passwords would you like to generate?")
passwordConstructCounter = 1
numOfPasswordCounter = 1
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
    password = ''
print("Here are your passwords:")
for x in passwordArray:
    print(str(passwordConstructCounter) + ". " + x)
    passwordConstructCounter += 1
wait_for_input()
#add fix for if input all of chars, just a quick if check
#put removed char versions into an array
#add file i/o

