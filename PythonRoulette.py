import random
import sys

from time import sleep

# Bullet.
shot= random.randint(0, 5)
# Current turns.
ammo= 0
# Cash.
money= 0

message= ["Very lucky huh?", "Lets continue.", "That was close."]
start_message= ["Lets get started then.", "Well done.", "Lets do it!"]
dead_message= ["You are dead.", "See you next life.", "Hahaha!"]

def trigger(current_shot):
    global money, shot, ammo, dead_message, message

    # If current shot had shot, end the game and reset all the variables.
    if current_shot == shot:
        print(random.choice(dead_message))
        sleep(1)
        print(f"You lose all your money.")
        sleep(1)
        money= 0
        ammo= 0
        shot= random.randint(0, 5)
        sys.exit()
    else:
        print(random.choice(message))
        money+= 1000
        ammo+= 1
        sleep(1)
        print(f"You earn ${money}")
        sleep(1)

def start():
    global ammo, run

    while True:
        pull_trigger= input("Do you want to pull the trigger? -> ")

        if pull_trigger.lower() == "y" or pull_trigger.lower() == "yes":
            trigger(ammo)
        else:
            print(f"You won ${money}")
            sleep(1)
            sys.exit()

# Main function, before starting the game.
def main():
    print("I put the ammo in a random slot.")
    sleep(2)
    print("Each time you pull you gets $1000.")
    sleep(2)
    print("If you died, you lose every of your money that you won.")
    sleep(2)
    print("Are you ready?")

    option= input("Yes/No? -> ")
   
    if option.lower() == "y" or option.lower() == "yes":
        print(random.choice(start_message))
        sleep(2)
        start()
    else:
        print("Are you scared?")
        sys.exit()

if __name__ == '__main__':
    main()