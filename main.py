import random
chars = 'abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()+|}{":?><,./;[]'
password = ''
passwordLength = input("How long would you like to make your password?")
while passwordLength <= 0 or passwordLength.is_integer() == False:  # Currently does not filter alphabetical inputs
    passwordLength = int(input("Please enter a valid numerical length."))
print(passwordLength)
removedCharacters = input("Which characters are disallowed?")  # Currently only allows removal of numbers and symbols
chars = chars.translate(None, str(removedCharacters))
for c in range(passwordLength):
    password += random.choice(chars)
print(password)
