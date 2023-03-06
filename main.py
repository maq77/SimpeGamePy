import random
import time


user_action = input("Enter a choice (rock, paper, scissors): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

sleep_3 = 3
time.sleep(sleep_3)
for i in range(sleep_3):
    print("Please Wait" , sleep_3)
    sleep_3 -= 1
    time.sleep(1)


time.sleep(1)

print("You Chose  " + user_action + " and Computer Chose " + computer_action)

time.sleep(3)
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
