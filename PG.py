import random
from random import *
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

class Password_generator:

    def __init__(self):
        self. user_password = ("")


    def create_password(self):
        self.user_password = ("")
        self.password = [letters[randint(0, len(letters)-1)] for x in range (0, randint(3, 7))]
        self.password += [symbols[randint(0, len(symbols) - 1)] for x in range(0, randint(2, 4))]
        self.password += [numbers[randint(0, len(numbers) - 1)] for x in range(0, randint(2, 4))]
        shuffle(self.password)
        self.user_password = "".join([i for i in self.password])

