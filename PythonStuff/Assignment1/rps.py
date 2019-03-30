# Incorporate the random library
import random


# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)



# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == "r" and user_choice == "s" :
    print ("computer wins")
elif computer_choice == "p" and user_choice == "r" :
    print ("computer wins")
elif computer_choice == "s" and user_choice == "p" :
    print ("computer wins")
elif computer_choice == "s" and user_choice == "r" :
    print ("YOU WIN!!")
elif computer_choice == "r" and user_choice == "p" :
    print ("YOU WIN!!")
elif computer_choice == "p" and user_choice == "s" :
    print ("YOU WIN!!")

print(computer_choice)

