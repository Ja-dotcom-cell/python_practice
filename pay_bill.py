#who will pay the bill in the restaurant?

import random

name= input("Enter the names  separating each name by comma: ")

name_split = name.split(",")
name_length = len(name_split)
random_choice = random.randint(0, name_length-1)
print(f"{name_split[random_choice]} will pay the bill.")

