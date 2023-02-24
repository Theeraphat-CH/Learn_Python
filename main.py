import random

random.number = random.randint(1, 10)
tries = 1

username = input("Hello, What your username : ")

print("Hello", username + "," ,)

question = input("Would ypu like to play a game? [Y/N] : ")


if question == "n" or question == "N":
    print("Byeee")
elif question == "y" or question == "Y":
    pass