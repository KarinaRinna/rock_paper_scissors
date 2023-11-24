import random

user_wins = 0
computer_wins = 0

options = ["камень", "бумага", "ножницы"]
options[0]

while True:
    user_input = input("Введите Камень/Ножницы/Бумага или 'выйти' чтобы выйти: ").lower()
    if user_input == "выйти":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper:1, scissors: 2
    computer_pick = options[random_number]
    print("Компьютер выбрал", computer_pick + ".")

    if user_input == "камень" and computer_pick == "ножницы":
        print("Вы выйграли!")
        user_wins += 1
        continue

    elif user_input == "бумага" and computer_pick == "камень":
        print("Вы выйграли!")
        user_wins += 1

    elif user_input == "ножницы" and computer_pick == "бумага":
        print("Вы выйграли!")
        user_wins += 1
        
    elif user_input == "ножницы" and computer_pick == "ножницы" or user_input == "бумагп" and computer_pick == "бумага" or user_input == "камень" and computer_pick == "камень":
        print("Ничья!")

    else:
        print("Вы проиграли!")
        computer_wins += 1


print("Вы выйграли", user_wins, "раз.")
print("Компьютер выграл", computer_wins, "раз.")
print("Конец игры!")