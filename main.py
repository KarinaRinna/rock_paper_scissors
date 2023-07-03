import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Введите Камень/Ножницы/Бумага или Q чтобы выйти")
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper:1, scissors: 2
    computer_pick = options[random_number]
    print("Компьютер выбрал", computer_pick + ".")

    