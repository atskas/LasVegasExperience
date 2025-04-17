import random
import time
import sys
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get the path to the moneystore.txt file in the same directory as the script
money_store = os.path.join(script_directory, 'moneystore.txt')

user_input = input('Do you want to gamble? (y/n): ').lower()

# Function to gamble :money_mouth:
def gamble():
    # Open the file in read mode and get the current balance
    with open(money_store, 'r') as money:
        current_money = int(money.read().strip())  # Convert the balance to an integer

    if user_input == 'y':
        if current_money > 0:
            chance = 40  # Chance of winning

            # Determine win or loss based on a random number
            if random.randint(0, 100) < chance:
                new_money = current_money * 2  # Double the balance if you win
                # Save the new balance to the file
                with open(money_store, 'w') as money_writer:
                    money_writer.write(str(new_money))
                print(f"New Balance: {new_money}$")  # Display the updated balance after winning
            else:
                new_money = current_money // 2  # Halve the balance if you lose
                # Save the new balance to the file
                with open(money_store, 'w') as money_writer:
                    money_writer.write(str(new_money))
                print(f"New Balance: {new_money}$")  # Display the updated balance after losing
        else:
            print("Not enough money, come back another time.")
            time.sleep(3) 
            sys.exit()
    elif user_input == 'n':
        print("You made a good decision.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Main loop to repeatedly ask if YOU want to gamble or exit
while True:
    gamble()  # Run the gamble function once
    again = input("Do you want to gamble again? (y/n): ").lower()
    
    if again == 'n':
        print("Come back again. You know you will.")
        time.sleep(3)
        break  # Exit the loop, we all know you'll come back.
