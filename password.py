MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 14

password = input("Enter your password: ")
password_length = len(password)

while password_length >= MIN_PASSWORD_LENGTH or password_length <= MAX_PASSWORD_LENGTH:

    if password.isalpha():
        print("Your password is weak!")

    elif password.isnumeric():

        print("Your password is weak!")

    else:

        print("Your password is strong!")

print("Number of characters used in password: ", password_length,"the min length expected is: ",MIN_PASSWORD_LENGTH,
"the max length is: ", MAX_PASSWORD_LENGTH)