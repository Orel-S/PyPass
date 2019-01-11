import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()+|}{":?><,./;[]'
password = ''
passwordArray = []
numOfPasswords = int(input("How many passwords would you like to generate?"))
counter = 1
for p in range(numOfPasswords):
    passwordLength = input("How long would you like to make your password?")
    while passwordLength <= 0 or type(passwordLength) == float:  # Currently does not filter alphabetical inputs
        passwordLength = int(input("Please enter a valid numerical length."))
    print(passwordLength)
    removedCharacters = input("Which characters are disallowed?")  # Currently only allows removal of numbers and symbols
    chars = chars.translate(None, str(removedCharacters))
    for c in range(passwordLength):
        password += random.choice(chars)
    passwordArray.append(password)
    password = ''
print("Here are your passwords:")
for x in passwordArray:
    print(str(counter) + ". " + x)
    counter += 1
input()
