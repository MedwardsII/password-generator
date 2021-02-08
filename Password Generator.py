# Password Generator
# App allowing for the automatic creation of passwords

import random
import string


print("Welcome to Password Generator!")


class Password:

    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.punctuation = string.punctuation

    def get_pass_len_req(self):
        return self.pass_len_req

    def get_password(self, password_length, has_digits, has_special_char):

        option_blend = self.letters

        if has_digits is True:
            option_blend += self.digits

        if has_special_char is True:
            option_blend += self.punctuation

        password_gen = ""

        for n in range(password_length):
            password_gen += str(option_blend[random.randrange(0, len(option_blend))])

        return password_gen

password = Password()

# Creating new random password
pass_ran_len = random.randrange(8, 16)
new_password = password.get_password(pass_ran_len, True, True)
print(f"Suggested Password: {new_password}")

while(True):
    try:
        continue_gen = input("Generate new password? (y/n): ")
        assert continue_gen.lower() == "y" or continue_gen.lower() == "n"

        if continue_gen.lower() == "n":
            print("Thank you and have a great day!")
            break

        while True:
            try:
                password_length = int(input("Password length: "))
                break
            except ValueError:
                print("Please select a numerical value of 8 or higher!")
            except:
                print("Error! Please try again!")

        while True:
            try:
                has_special_char = input("Use special characters? (y/n): ")
                assert has_special_char.lower() == "y" or has_special_char.lower() == "n"
                has_digits = input("Use numbers? (y/n): ")
                assert has_digits.lower() == "y" or has_digits.lower() == "n"
                break
            except AssertionError:
                print("Please Enter (Y)es or (N)o to continue!")

        if has_special_char == "y":
            has_special_char = True

        if has_digits == "y":
            has_digits = True

        new_password = password.get_password(password_length, has_digits, has_special_char)

        print(f"NEW PASSWORD: {new_password}")

    except AssertionError:
        print("Please Enter (Y)es or (N)o to continue!")
