import random

response = "y"

while response.lower() == "y":
    dice_number = random.randint(1, 6)
    print("The dice shows:", dice_number)
    response = input("Do you want to roll the dice again? (y/n): ")