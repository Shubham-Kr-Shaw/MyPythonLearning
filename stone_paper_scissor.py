import random
lst = ["1","2","3"]

chance = 10
current_chance = 0
computer_score = 0
human_score = 0

print("\t \t \t Let's Play Stone, Paper, Scissor")
print("Press 1 for stone. \nPress 2 for Paper. \nPress 3 for Scissor.\n")

while current_chance < chance:
    _input = input("Stone, Paper, Scissor : ")
    _random = random.choice(lst)

    if _input == _random:
        print("Tie Both 0 point to each \n")

    elif _input == "1" and _random == "2":
        computer_score = computer_score + 1
        print("Aww..! Stone is wrapped by paper You loose.\n")
        print("Computer wins 1 point \n")
        print(f"computer_score is {computer_score} and your point is {human_score} \n")

    elif _input == "1" and _random =="3":
        human_score = human_score + 1
        print("Yea..! Stone brock the Scissor into pieces.\n")
        print("You won and you get 1 point \n")
        print(f"computer_score is {computer_score} and your Score is {human_score} \n")

    elif _input == "2" and _random =="1":
        human_score = human_score + 1
        print("Aww..! Stone is wrapped by paper You win.\n")
        print("You won and you get 1 point \n")
        print(f"computer_score is {computer_score} and your Score is {human_score} \n")

    elif _input == "2" and _random =="3":
        computer_score = computer_score + 1
        print("Aww..! Scissoris croped the paper and You loose.\n")
        print("Computer wins 1 point \n")
        print(f"computer_score is {computer_score} and your score is {human_score} \n")

    elif _input == "3" and _random =="1":
        computer_score = computer_score + 1
        print("Yea..! Stone brock the Scissor into pieces.\n")
        print("Computer wins 1 point \n")
        print(f"computer_score is {computer_score} and your Score is {human_score} \n")

    elif _input == "3" and _random =="2":
        human_score = human_score + 1
        print("Aww..! Scissoris croped the paper and You loose.\n")
        print("You won and you get 1 point \n")
        print(f"computer_score is {computer_score} and your Score is {human_score} \n")

    else:
        print("Both chossed the same, Better luck next time")

    current_chance = current_chance + 1
    print(f"You can try {chance - current_chance} time only\n")

print("\t \t \tGAME OVER")

if computer_score == human_score:
    print("Tie")

elif computer_score > human_score:
    print("Computer wins and you loose")

else:
    print("You win and computer loose")

print(f"Your point is {human_score} and computer point is {computer_score}")
