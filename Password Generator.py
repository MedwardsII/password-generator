# Password Generator
# App allowing for the automatic creation of passwords

import random
import string


print("Welcome to Password Generator!")


class Password:

    def __init__(self):
        self.pass_len_req = 8
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.punctuation = string.punctuation

    def get_pass_len_req(self):
        return self.pass_len_req

    def get_password(self, password_length, has_special_char):

        option_blend = self.letters + self.digits

        if has_special_char == True:
            option_blend += self.punctuation

        password_gen = ""

        for n in range(password_length):
            password_gen += str(option_blend[random.randrange(0, len(option_blend))])

        return password_gen

while(True):
    try:
        password = Password()

        while True:
            try:
                password_length = int(input("Password length: "))
                assert password_length >= password.get_pass_len_req()
                break
            except ValueError:
                print("Please select a numerical value of 8 or higher!")
            except:
                print("Suggested minimum password length is 8 characters!")

        while True:
            try:
                has_special_char = input("Use special characters? (y/n): ")
                assert has_special_char.lower() == "y" or has_special_char.lower() == "n"
                break
            except AssertionError:
                print("Please Enter (Y)es or (N)o to continue!")

        if has_special_char == "y":
            has_special_char = True

        new_password = password.get_password(password_length, has_special_char)

        print(f"NEW PASSWORD: {new_password}")

        continue_gen = input("Generate new password? (y/n): ")
        assert continue_gen.lower() == "y" or continue_gen.lower() == "n"

        if continue_gen.lower() == "n":
            print("Thank you and have a great day!")
            break

    except AssertionError:
        print("Please Enter (Y)es or (N)o to continue!")
